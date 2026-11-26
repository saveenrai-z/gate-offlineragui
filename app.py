import streamlit as st
import json
import re
from config import APP_TITLE, DEFAULT_LLM_MODEL
from database.db_manager import (
    init_db, get_all_subjects, get_chapters_by_subject,
    get_topics_by_chapter, update_topic_progress,
    get_pyqs, record_pyq_attempt
)
from modules.vector_store import VectorStore
from modules.llm_handler import LLMHandler
from modules.rag_pipeline import RAGPipeline
from modules.presentation_deck import PresentationDeckGenerator

# Page Configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Dark Shell + Crisp Presentation Canvas)
st.markdown("""
<style>
    /* Dark outer application shell */
    .stApp {
        background-color: #0B1120;
        color: #F8FAFC;
    }

    /* Professional Slide Deck Card */
    .deck-slide {
        background-color: #FAF9F6;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 32px 36px 20px 36px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
        color: #0F172A;
        margin-top: 8px;
        margin-bottom: 20px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    /* Category Tag (Top) */
    .deck-part {
        font-size: 0.88rem;
        font-weight: 800;
        letter-spacing: 2px;
        color: #A94A2D; /* Terracotta / Rust */
        text-transform: uppercase;
        margin-bottom: 6px;
    }

    /* Large Serif Slide Title */
    .deck-title {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 2.15rem;
        font-weight: 700;
        color: #1E293B;
        line-height: 1.25;
        margin-bottom: 4px;
    }

    /* Subtitle */
    .deck-sub {
        font-size: 0.98rem;
        color: #64748B;
        margin-bottom: 22px;
    }

    /* Multi-Column Grid */
    .deck-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-bottom: 20px;
    }

    /* Individual Column Cards */
    .deck-col {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 20px 16px;
        min-height: 250px;
        display: flex;
        flex-direction: column;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }

    .deck-col-header {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 1.22rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 12px;
        line-height: 1.3;
    }

    .deck-col-body {
        font-size: 0.93rem;
        color: #334155;
        line-height: 1.62;
        flex-grow: 1;
        white-space: pre-line;
    }

    /* Slide Bottom Area */
    .deck-bottom {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 16px;
        padding-top: 14px;
        border-top: 1px solid #E2E8F0;
    }

    .deck-summary {
        font-size: 0.96rem;
        color: #475569;
        font-style: italic;
    }

    .deck-page {
        font-size: 1.05rem;
        font-weight: 700;
        color: #64748B;
    }

    .deck-citation {
        font-size: 0.8rem;
        color: #94A3B8;
        margin-top: 8px;
    }

    /* Badges & Accents */
    .badge-offline {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.78rem;
        font-weight: 700;
        background-color: #10B981;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Core Services (FAISS 2,418 chunks & RAG)
@st.cache_resource
def load_core():
    init_db()
    vector_store = VectorStore(index_name="gate_faiss")
    llm_handler = LLMHandler(model_name=DEFAULT_LLM_MODEL)
    rag_pipeline = RAGPipeline(vector_store=vector_store, llm_handler=llm_handler)
    return vector_store, llm_handler, rag_pipeline

vector_store, llm_handler, rag_pipeline = load_core()

# State Management
if "nav_page" not in st.session_state:
    st.session_state["nav_page"] = "📖 Chapter Teachings"

if "topic_idx" not in st.session_state:
    st.session_state["topic_idx"] = 0

if "slide_idx" not in st.session_state:
    st.session_state["slide_idx"] = 0

if "slideshow_mode" not in st.session_state:
    st.session_state["slideshow_mode"] = False

# Navigation Callbacks (Unified Slide & Topic Progression)
def cb_prev_slide_or_topic():
    if st.session_state.get("slide_idx", 0) > 0:
        st.session_state["slide_idx"] -= 1
    elif st.session_state.get("topic_idx", 0) > 0:
        st.session_state["topic_idx"] -= 1
        st.session_state["slide_idx"] = 0

def cb_next_slide_or_topic(max_slides: int, max_topics: int):
    if st.session_state.get("slide_idx", 0) < max_slides - 1:
        st.session_state["slide_idx"] += 1
    elif st.session_state.get("topic_idx", 0) < max_topics - 1:
        st.session_state["topic_idx"] += 1
        st.session_state["slide_idx"] = 0

def cb_jump_slide(target_idx: int):
    st.session_state["slide_idx"] = target_idx

def cb_goto_teachings():
    st.session_state["nav_page"] = "📖 Chapter Teachings"

def cb_enter_slideshow():
    st.session_state["slideshow_mode"] = True

def cb_exit_slideshow():
    st.session_state["slideshow_mode"] = False

# Multi-Style Creative Slide Renderer
def render_deck_slide(slide: dict, curr_s_idx: int):
    layout = slide.get("layout", "cards")
    part = slide.get("part", "SYLLABUS LESSON")
    title = slide.get("title", "")
    sub = slide.get("subtitle", "")
    summary = slide.get("summary", "")
    footer = slide.get("footer", "")

    # STYLE 1: HERO DEFINITION + 2-COLUMN SPLIT
    if layout == "hero_split":
        hero = slide.get("hero", {})
        left = slide.get("left_card", {})
        right = slide.get("right_card", {})
        html_lines = [
            '<div class="deck-slide">',
            f'<div class="deck-part">{part}</div>',
            f'<div class="deck-title">{title}</div>',
            f'<div class="deck-sub">{sub}</div>',
            f'<div style="background-color: #EFF6FF; border-left: 6px solid #2563EB; border-radius: 8px; padding: 18px 24px; margin-bottom: 22px;">',
            f'<div style="font-size: 0.8rem; font-weight: 800; letter-spacing: 1.5px; color: #1D4ED8; margin-bottom: 4px;">{hero.get("badge", "CORE DEFINITION")}</div>',
            f'<div style="font-size: 1.05rem; color: #1E293B; line-height: 1.6;">{hero.get("text", "")}</div>',
            f'</div>',
            '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">',
            f'<div class="deck-col" style="border-top: 5px solid {left.get("color", "#2E6B4B")};">',
            f'<div class="deck-col-header">{left.get("header", "")}</div>',
            f'<div class="deck-col-body">{left.get("body", "")}</div>',
            f'</div>',
            f'<div class="deck-col" style="border-top: 5px solid {right.get("color", "#C25E38")};">',
            f'<div class="deck-col-header">{right.get("header", "")}</div>',
            f'<div class="deck-col-body">{right.get("body", "")}</div>',
            f'</div>',
            '</div>',
            '<div class="deck-bottom">',
            f'<div class="deck-summary"><em>{summary}</em></div>',
            f'<div class="deck-page">{curr_s_idx + 1}</div>',
            '</div>',
            f'<div class="deck-citation">📄 {footer}</div>',
            '</div>'
        ]

    # STYLE 1B: PIPELINE WORKFLOW (3-Stage Horizontal Flow)
    elif layout == "pipeline":
        stages = slide.get("stages", [])
        stage_cards = []
        for s in stages:
            stage_cards.append(
                f'<div style="background-color: #FFFFFF; border: 1px solid #E2E8F0; border-top: 6px solid {s.get("color", "#2563EB")}; border-radius: 10px; padding: 22px 18px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">'
                f'<div style="font-size: 0.78rem; font-weight: 800; color: {s.get("color", "#2563EB")}; letter-spacing: 1.5px; margin-bottom: 6px;">{s.get("step", "")}</div>'
                f'<div style="font-size: 1.25rem; font-weight: 700; color: #1E293B; margin-bottom: 10px; font-family: Georgia, serif;">{s.get("title", "")}</div>'
                f'<div style="color: #475569; font-size: 0.94rem; line-height: 1.6;">{s.get("desc", "")}</div>'
                f'</div>'
            )
        stages_joined = "".join(stage_cards)
        num_stages = len(stages)
        html_lines = [
            '<div class="deck-slide">',
            f'<div class="deck-part">{part}</div>',
            f'<div class="deck-title">{title}</div>',
            f'<div class="deck-sub">{sub}</div>',
            f'<div style="display: grid; grid-template-columns: repeat({num_stages}, 1fr); gap: 18px; margin-bottom: 22px;">{stages_joined}</div>',
            '<div class="deck-bottom">',
            f'<div class="deck-summary"><em>{summary}</em></div>',
            f'<div class="deck-page">{curr_s_idx + 1}</div>',
            '</div>',
            f'<div class="deck-citation">📄 {footer}</div>',
            '</div>'
        ]

    # STYLE 2: WORKED NUMERICAL EXAMPLE
    elif layout == "worked_example":
        problem = slide.get("problem", "")
        steps = slide.get("steps", [])
        answer = slide.get("answer", "")
        steps_html = []
        for s in steps:
            steps_html.append(
                f'<div style="background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 6px; padding: 14px 18px; margin-bottom: 10px;">'
                f'<div style="font-weight: 700; color: #1D4ED8; font-size: 0.95rem; margin-bottom: 4px;">{s.get("step_num", "")}</div>'
                f'<div style="color: #334155; font-size: 0.94rem; line-height: 1.5;">{s.get("text", "")}</div>'
                f'</div>'
            )
        steps_joined = "".join(steps_html)

        html_lines = [
            '<div class="deck-slide">',
            f'<div class="deck-part">{part}</div>',
            f'<div class="deck-title">{title}</div>',
            f'<div class="deck-sub">{sub}</div>',
            f'<div style="background-color: #FEF3C7; border-left: 6px solid #D97706; border-radius: 8px; padding: 16px 22px; margin-bottom: 18px;">'
            f'<div style="font-size: 0.8rem; font-weight: 800; letter-spacing: 1.5px; color: #92400E; margin-bottom: 4px;">PROBLEM STATEMENT</div>'
            f'<div style="font-size: 1.02rem; color: #78350F; line-height: 1.6;">{problem}</div>'
            f'</div>',
            f'<div style="margin-bottom: 16px;">{steps_joined}</div>',
            f'<div style="background-color: #ECFDF5; border: 2px solid #059669; border-radius: 8px; padding: 14px 20px; font-size: 1.05rem; font-weight: 700; color: #065F46; margin-bottom: 16px;">'
            f'{answer}'
            f'</div>',
            '<div class="deck-bottom">',
            f'<div class="deck-summary"><em>{summary}</em></div>',
            f'<div class="deck-page">{curr_s_idx + 1}</div>',
            '</div>',
            f'<div class="deck-citation">📄 {footer}</div>',
            '</div>'
        ]

    # STYLE 3: COMPARATIVE MATRIX / 2-COLUMN BOARD
    elif layout == "comparison":
        left = slide.get("left", {})
        right = slide.get("right", {})
        l_pts = "".join([f'<li style="margin-bottom: 10px; color: #334155;">{p}</li>' for p in left.get("points", [])])
        r_pts = "".join([f'<li style="margin-bottom: 10px; color: #334155;">{p}</li>' for p in right.get("points", [])])
        html_lines = [
            '<div class="deck-slide">',
            f'<div class="deck-part">{part}</div>',
            f'<div class="deck-title">{title}</div>',
            f'<div class="deck-sub">{sub}</div>',
            '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">',
            f'<div style="background-color: #FFFFFF; border: 2px solid {left.get("color", "#2563EB")}; border-radius: 10px; padding: 22px 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">'
            f'<div style="background-color: {left.get("color", "#2563EB")}; color: white; padding: 6px 14px; border-radius: 6px; font-weight: 800; font-size: 0.85rem; letter-spacing: 1px; display: inline-block; margin-bottom: 16px;">{left.get("badge", "")}</div>'
            f'<ul style="padding-left: 20px; margin: 0; line-height: 1.6;">{l_pts}</ul>'
            f'</div>',
            f'<div style="background-color: #FFFFFF; border: 2px solid {right.get("color", "#7C3AED")}; border-radius: 10px; padding: 22px 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">'
            f'<div style="background-color: {right.get("color", "#7C3AED")}; color: white; padding: 6px 14px; border-radius: 6px; font-weight: 800; font-size: 0.85rem; letter-spacing: 1px; display: inline-block; margin-bottom: 16px;">{right.get("badge", "")}</div>'
            f'<ul style="padding-left: 20px; margin: 0; line-height: 1.6;">{r_pts}</ul>'
            f'</div>',
            '</div>',
            '<div class="deck-bottom">',
            f'<div class="deck-summary"><em>{summary}</em></div>',
            f'<div class="deck-page">{curr_s_idx + 1}</div>',
            '</div>',
            f'<div class="deck-citation">📄 {footer}</div>',
            '</div>'
        ]

    # STYLE 4: EXAM TRAPS & NAT REVISION DASHBOARD
    elif layout == "traps_dashboard":
        traps = slide.get("traps", [])
        t_cards = []
        for t in traps:
            t_cards.append(
                f'<div style="background-color: #FFFFFF; border-left: 6px solid {t.get("color", "#DC2626")}; border-radius: 8px; padding: 18px 20px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">'
                f'<div style="font-weight: 800; font-size: 1.05rem; color: #1E293B; margin-bottom: 6px;">{t.get("icon", "⚠️")} {t.get("title", "")}</div>'
                f'<div style="color: #475569; font-size: 0.95rem; line-height: 1.6;">{t.get("desc", "")}</div>'
                f'</div>'
            )
        t_joined = "".join(t_cards)
        html_lines = [
            '<div class="deck-slide">',
            f'<div class="deck-part">{part}</div>',
            f'<div class="deck-title">{title}</div>',
            f'<div class="deck-sub">{sub}</div>',
            f'<div style="margin-bottom: 20px;">{t_joined}</div>',
            '<div class="deck-bottom">',
            f'<div class="deck-summary"><em>{summary}</em></div>',
            f'<div class="deck-page">{curr_s_idx + 1}</div>',
            '</div>',
            f'<div class="deck-citation">📄 {footer}</div>',
            '</div>'
        ]

    # STYLE 5: 4-COLUMN CARDS (User reference style)
    else:
        col_cards = []
        cols_data = slide.get("columns", [])
        num_cols = len(cols_data)
        for col in cols_data:
            body_text = col["body"].replace("\n", "<br>")
            col_cards.append(
                f'<div class="deck-col" style="border-top: 5px solid {col["color"]};">'
                f'<div class="deck-col-header">{col["header"]}</div>'
                f'<div class="deck-col-body">{body_text}</div>'
                f'</div>'
            )
        cols_joined = "".join(col_cards)
        grid_template = f"repeat({max(num_cols, 1)}, 1fr)"
        html_lines = [
            '<div class="deck-slide">',
            f'<div class="deck-part">{part}</div>',
            f'<div class="deck-title">{title}</div>',
            f'<div class="deck-sub">{sub}</div>',
            f'<div class="deck-grid" style="grid-template-columns: {grid_template};">{cols_joined}</div>',
            '<div class="deck-bottom">',
            f'<div class="deck-summary"><em>{summary}</em></div>',
            f'<div class="deck-page">{curr_s_idx + 1}</div>',
            '</div>',
            f'<div class="deck-citation">📄 {footer}</div>',
            '</div>'
        ]

    clean_html = "\n".join(l.strip() for l in html_lines)
    st.markdown(clean_html, unsafe_allow_html=True)

# TRUE FULLSCREEN SLIDESHOW MODE
if st.session_state.get("slideshow_mode", False) and st.session_state["nav_page"] == "📖 Chapter Teachings":
    st.markdown("""
    <style>
        [data-testid="stSidebar"] { display: none !important; }
        header[data-testid="stHeader"] { display: none !important; }
        footer { display: none !important; }
        .main .block-container {
            max-width: 98vw !important;
            padding: 1rem 2rem !important;
            margin: 0 auto !important;
        }
        .deck-slide {
            min-height: 72vh !important;
            padding: 34px 44px !important;
            box-shadow: 0 16px 48px rgba(0,0,0,0.6) !important;
            border: 2px solid #38BDF8 !important;
        }
        .deck-title {
            font-size: 2.6rem !important;
        }
        .deck-col {
            min-height: 290px !important;
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation (only rendered when NOT in fullscreen slideshow)
if not st.session_state.get("slideshow_mode", False):
    with st.sidebar:
        st.markdown("### 🎓 GATE AI TUTOR")
        st.markdown('<span class="badge-offline">100% OFFLINE</span>', unsafe_allow_html=True)
        st.write("")

        menu_options = [
            "📊 Dashboard",
            "📖 Chapter Teachings",
            "❓ Ask Doubts",
            "📝 Previous Year Questions",
            "🎯 Practice Questions",
            "⚡ Formula Cheat Sheets"
        ]

        selected_menu = st.radio(
            "Menu",
            options=menu_options,
            index=menu_options.index(st.session_state["nav_page"]) if st.session_state["nav_page"] in menu_options else 1,
            key="app_menu_radio"
        )
        if selected_menu != st.session_state["nav_page"]:
            st.session_state["nav_page"] = selected_menu
            st.rerun()

        st.markdown("---")
        st.caption("GATE Paper: Data Science & AI (DA)")
        ollama_status = llm_handler.check_ollama_status()
        st.caption(f"Local AI Daemon: {'🟢 Running' if ollama_status['running'] else '🟡 Standby / Offline RAG'}")
        st.caption("Knowledge Base: 2,418 Chunks (FAISS)")

# -------------------------------------------------------------
# 1. DASHBOARD VIEW (Clean, No Numbers/Counter Boxes)
# -------------------------------------------------------------
if st.session_state["nav_page"] == "📊 Dashboard":
    st.title("GATE Preparation Dashboard")
    st.caption("Official Syllabus-Based AI Tutor for GATE Data Science & AI (DA)")
    st.write("")

    st.markdown("""
    <div style="background-color: #1E293B; border-radius: 12px; padding: 28px; border: 1px solid #334155; margin-bottom: 24px;">
        <h3 style="color: #F8FAFC; margin-top: 0; font-family: Georgia, serif;">Syllabus-Grounded Learning Environment</h3>
        <p style="color: #CBD5E1; font-size: 1.05rem; line-height: 1.6;">
            Learn step-by-step through structured PPT slides extracted directly from your assigned textbooks.
            Everything runs 100% offline using local vector search over 2,418 pre-indexed syllabus chunks.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_btn, _ = st.columns([1.5, 3])
    with col_btn:
        st.button("Continue Learning ➔", type="primary", on_click=cb_goto_teachings, key="btn_dash_learn", use_container_width=True)

    st.write("")
    st.subheader("Syllabus Subjects & Textbook Mapping")
    subjects = get_all_subjects()
    sub_cols = st.columns(2)
    for idx, sub in enumerate(subjects):
        with sub_cols[idx % 2]:
            chaps = get_chapters_by_subject(sub["id"])
            with st.expander(f"📘 {sub['name']}"):
                for c in chaps:
                    st.markdown(f"• **{c['title']}**")

# -------------------------------------------------------------
# 2. CHAPTER TEACHINGS (SLIDE DECK VIEW + TRUE SLIDESHOW)
# -------------------------------------------------------------
elif st.session_state["nav_page"] == "📖 Chapter Teachings":
    subjects = get_all_subjects()
    if not subjects:
        st.error("No subjects registered in the database.")
        st.stop()

    is_slideshow = st.session_state.get("slideshow_mode", False)

    # In slideshow mode: Floating top control bar
    if is_slideshow:
        fs_bar1, fs_bar2 = st.columns([4, 1])
        with fs_bar1:
            st.markdown(f"**🖥️ SLIDESHOW MODE** &nbsp;|&nbsp; *Press button on right to return to standard view*")
        with fs_bar2:
            st.button("🗗 Exit Slideshow", on_click=cb_exit_slideshow, type="primary", key="btn_exit_fs", use_container_width=True)

    # Standard header controls (hidden in pure slideshow)
    if not is_slideshow:
        c_s1, c_s2, c_fs = st.columns([2, 2, 1])
        with c_s1:
            sel_sub_name = st.selectbox("Subject", [s["name"] for s in subjects], key="deck_sub_select")
            sel_sub = next(s for s in subjects if s["name"] == sel_sub_name)

        chapters = get_chapters_by_subject(sel_sub["id"])
        with c_s2:
            chap_titles = [c["title"] for c in chapters] if chapters else ["None"]
            sel_chap_title = st.selectbox("Chapter", chap_titles, key="deck_chap_select")
            sel_chap = next((c for c in chapters if c["title"] == sel_chap_title), None)

        with c_fs:
            st.write("")
            st.write("")
            st.button("⛶ Slideshow Mode", on_click=cb_enter_slideshow, key="btn_enter_fs", use_container_width=True)
    else:
        # In slideshow mode, retain active subject and chapter
        sel_sub_name = st.session_state.get("deck_sub_select", subjects[0]["name"])
        sel_sub = next(s for s in subjects if s["name"] == sel_sub_name)
        chapters = get_chapters_by_subject(sel_sub["id"])
        sel_chap_title = st.session_state.get("deck_chap_select", chapters[0]["title"] if chapters else "None")
        sel_chap = next((c for c in chapters if c["title"] == sel_chap_title), chapters[0] if chapters else None)

    # Track subject/chapter changes to reset progression cleanly
    if ("last_deck_sub" in st.session_state and st.session_state["last_deck_sub"] != sel_sub_name) or \
       ("last_deck_chap" in st.session_state and st.session_state["last_deck_chap"] != sel_chap_title):
        st.session_state["topic_idx"] = 0
        st.session_state["slide_idx"] = 0

    st.session_state["last_deck_sub"] = sel_sub_name
    st.session_state["last_deck_chap"] = sel_chap_title

    if sel_chap:
        topics = get_topics_by_chapter(sel_chap["id"])
        total_topics = len(topics)

        if total_topics == 0:
            st.warning("No topics registered for this chapter.")
        else:
            cur_t_idx = min(max(0, st.session_state.get("topic_idx", 0)), total_topics - 1)
            st.session_state["topic_idx"] = cur_t_idx

            if not is_slideshow:
                c_t1, c_t2 = st.columns([3, 1])
                with c_t1:
                    topic_titles = [t["title"] for t in topics]
                    chosen_title = st.selectbox(
                        "Select Topic to Study:",
                        options=topic_titles,
                        index=cur_t_idx,
                        key=f"deck_topic_select_{cur_t_idx}"
                    )
                    if chosen_title != topic_titles[cur_t_idx]:
                        new_idx = topic_titles.index(chosen_title)
                        st.session_state["topic_idx"] = new_idx
                        st.session_state["slide_idx"] = 0
                        st.rerun()
                with c_t2:
                    st.write("")
                    st.write("")
                    st.markdown(f"**Step {cur_t_idx + 1} of {total_topics}**")

            curr_topic = topics[st.session_state["topic_idx"]]

            # Load presentation deck
            deck = PresentationDeckGenerator.get_deck(
                subject_name=sel_sub_name,
                chapter_title=sel_chap_title,
                topic_title=curr_topic["title"]
            )
            total_slides = len(deck)

            if st.session_state["slide_idx"] >= total_slides:
                st.session_state["slide_idx"] = 0

            curr_s_idx = st.session_state["slide_idx"]
            slide = deck[curr_s_idx]

            # Progress Bar
            st.progress((curr_s_idx + 1) / total_slides)

            # RENDER THE CREATIVE PRESENTATION SLIDE
            render_deck_slide(slide, curr_s_idx)

            # Interactive Slide Navigation Controls (Unified Slide & Topic Progression)
            c_prev, c_pills, c_next = st.columns([1.2, 2.5, 1.2])

            with c_prev:
                has_prev = (curr_s_idx > 0) or (st.session_state["topic_idx"] > 0)
                st.button(
                    "⬅ Previous Slide",
                    disabled=not has_prev,
                    on_click=cb_prev_slide_or_topic,
                    key="action_btn_prev",
                    use_container_width=True
                )

            with c_pills:
                pill_cols = st.columns(total_slides)
                for p_i in range(total_slides):
                    with pill_cols[p_i]:
                        is_active = (p_i == curr_s_idx)
                        btn_txt = f"👉 {p_i + 1}" if is_active else f"{p_i + 1}"
                        st.button(
                            btn_txt,
                            key=f"slide_pill_btn_{p_i}",
                            type="primary" if is_active else "secondary",
                            on_click=cb_jump_slide,
                            args=(p_i,),
                            use_container_width=True
                        )

            with c_next:
                if curr_s_idx < total_slides - 1:
                    st.button(
                        "Next Slide ➡",
                        type="primary",
                        on_click=cb_next_slide_or_topic,
                        args=(total_slides, total_topics),
                        key="action_btn_next",
                        use_container_width=True
                    )
                elif st.session_state["topic_idx"] < total_topics - 1:
                    nxt_topic_name = topics[st.session_state["topic_idx"] + 1]["title"]
                    st.button(
                        f"Next Topic: {nxt_topic_name[:20]}... ⏩",
                        type="primary",
                        on_click=cb_next_slide_or_topic,
                        args=(total_slides, total_topics),
                        key="action_btn_next_topic",
                        use_container_width=True
                    )
                else:
                    st.success("🎉 You completed all topics in this chapter!")

            # Topic Completion Toggle (only in normal view)
            if not is_slideshow:
                st.write("")
                is_done = curr_topic["completed"] == 1
                new_done = st.checkbox("Mark topic as completed", value=is_done, key=f"topic_chk_{curr_topic['id']}")
                if new_done != is_done:
                    update_topic_progress(curr_topic["id"], completed=1 if new_done else 0)
                    st.rerun()

# -------------------------------------------------------------
# 3. ASK DOUBTS (OFFLINE EXPERT GATE TUTOR)
# -------------------------------------------------------------
elif st.session_state["nav_page"] == "❓ Ask Doubts":
    st.title("❓ AI Doubt Solver")
    st.caption("Ask any question on the syllabus to receive rigorous, step-by-step mathematical explanations.")
    st.write("")

    subjects = get_all_subjects()
    sub_opts = ["All Subjects"] + [s["name"] for s in subjects]
    doubt_sub = st.selectbox("Subject Focus (Optional)", sub_opts, key="doubt_sub_filter")

    user_query = st.text_area(
        "Enter your question or doubt:", 
        placeholder="e.g. give me more about gradient vector. Or explain sample space and events.", 
        height=100
    )

    if st.button("Get Instant Explanation 🔍", type="primary", key="btn_ask_doubt"):
        if not user_query.strip():
            st.warning("Please enter a question or doubt.")
        else:
            with st.spinner("Searching syllabus materials and generating grounded explanation..."):
                filter_val = None if doubt_sub == "All Subjects" else doubt_sub
                res = rag_pipeline.query(question=user_query, subject_filter=filter_val, top_k=4, general_mode=True)

                st.markdown("---")
                st.markdown(res["answer"])

                if res.get("sources"):
                    st.write("")
                    st.markdown("##### 📄 Verified Textbook Sources")
                    for src in res["sources"]:
                        st.caption(f"• **{src.get('source_file', 'GATE Textbook')}** (Page {src.get('page', 1)}) — Subject: `{src.get('subject', 'General')}`")

# -------------------------------------------------------------
# 4. PREVIOUS YEAR QUESTIONS (PYQs)
# -------------------------------------------------------------
elif st.session_state["nav_page"] == "📝 Previous Year Questions":
    st.title("📝 GATE Previous Year Questions (PYQs)")
    st.caption("119 Authentic Exam Questions from GATE Data Science & AI (2024, 2025) and CS Papers.")
    st.write("")

    col_f1, col_f2 = st.columns(2)
    with col_f1:
        subjects = get_all_subjects()
        pyq_sub_filter = st.selectbox("Filter Subject", ["All Subjects"] + [s["name"] for s in subjects], key="pyq_filter_sub")
    with col_f2:
        pyq_year_filter = st.selectbox("Filter Year / Paper", ["All Years", "2025", "2024"], key="pyq_filter_yr")

    sub_arg = None if pyq_sub_filter == "All Subjects" else pyq_sub_filter
    yr_arg = int(pyq_year_filter) if pyq_year_filter != "All Years" else None

    pyqs = get_pyqs(gate_paper=None, year=yr_arg, subject=sub_arg)

    if not pyqs:
        st.info("No questions found matching your filter criteria.")
    else:
        st.write(f"Showing **{len(pyqs)}** questions:")
        for idx, q in enumerate(pyqs[:25]):
            with st.container():
                st.markdown(f"#### Q{idx + 1}. [{q.get('gate_paper', 'GATE')} {q.get('year', '')}] (Marks: {q.get('marks', 1)})")
                st.markdown(f"**{q['question_text']}**")

                opts = []
                opt_map = {}
                for opt_key in ["option_a", "option_b", "option_c", "option_d"]:
                    val = q.get(opt_key, "")
                    if val:
                        letter = opt_key.split("_")[1].upper()
                        opts.append(f"({letter}) {val}")
                        opt_map[f"({letter}) {val}"] = letter

                if opts:
                    user_ans = st.radio(f"Select Answer for Q{idx + 1}:", opts, key=f"radio_pyq_{q['id']}")
                    
                    if st.button(f"Submit Q{idx + 1}", key=f"submit_pyq_{q['id']}"):
                        selected_letter = opt_map.get(user_ans, "")
                        correct_letter = q.get("correct_answer", "").strip().upper()

                        is_correct = (selected_letter == correct_letter)
                        record_pyq_attempt(q["id"], selected_letter, is_correct)

                        if is_correct:
                            st.success(f"✅ Correct! The correct answer is ({correct_letter}).")
                        else:
                            st.error(f"❌ Incorrect. You selected ({selected_letter}), but the correct answer is ({correct_letter}).")

                        if q.get("explanation"):
                            st.info(f"**Explanation:**\n{q['explanation']}")
                else:
                    st.caption("Numerical Answer Type (NAT)")
                    with st.expander("View Correct Answer & Solution"):
                        st.markdown(f"**Correct Answer:** {q.get('correct_answer', 'N/A')}")
                        if q.get("explanation"):
                            st.markdown(f"**Explanation:** {q['explanation']}")
                st.markdown("---")

# -------------------------------------------------------------
# 5. PRACTICE QUESTIONS
# -------------------------------------------------------------
elif st.session_state["nav_page"] == "🎯 Practice Questions":
    st.title("🎯 Topic Practice MCQs")
    st.caption("Consolidate concepts through verified exam questions.")
    st.write("")

    subjects = get_all_subjects()
    sel_sub = st.selectbox("Select Subject", [s["name"] for s in subjects], key="prac_sub")
    sub_obj = next(s for s in subjects if s["name"] == sel_sub)
    chaps = get_chapters_by_subject(sub_obj["id"])
    sel_chap = st.selectbox("Select Chapter", [c["title"] for c in chaps] if chaps else ["None"], key="prac_chap")

    st.markdown(f"""
    <div style="background-color: #1E293B; padding: 20px; border-radius: 8px; border: 1px solid #334155;">
        <h4 style="margin-top: 0; color: #F8FAFC;">Practice Quiz for {sel_chap}</h4>
        <p style="color: #94A3B8;">
            Select options below to test your theoretical and mathematical accuracy.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    st.markdown("**Q1. If events A and B are mutually exclusive with P(A) > 0 and P(B) > 0, what is P(A|B)?**")
    ans_q1 = st.radio("Options:", ["(A) P(A)", "(B) 0", "(C) 1", "(D) P(A) · P(B)"], key="quiz_q1")
    if st.button("Check Q1 Answer", key="btn_check_q1"):
        if "(B)" in ans_q1:
            st.success("✅ Correct! Since A ∩ B = ∅, P(A ∩ B) = 0. Therefore P(A|B) = P(A ∩ B) / P(B) = 0.")
        else:
            st.error("❌ Incorrect. The correct answer is (B) 0. Mutually exclusive events cannot occur simultaneously.")

    st.markdown("---")
    st.markdown("**Q2. Under what condition is the union of two vector subspaces U and W guaranteed to be a subspace?**")
    ans_q2 = st.radio("Options:", ["(A) Always", "(B) If and only if U ⊆ W or W ⊆ U", "(C) If U ∩ W = {0}", "(D) Never"], key="quiz_q2")
    if st.button("Check Q2 Answer", key="btn_check_q2"):
        if "(B)" in ans_q2:
            st.success("✅ Correct! A union of two subspaces is itself a subspace if and only if one is contained within the other.")
        else:
            st.error("❌ Incorrect. The correct answer is (B). If neither is contained in the other, vector addition escapes the union.")

# -------------------------------------------------------------
# 6. FORMULA CHEAT SHEETS
# -------------------------------------------------------------
elif st.session_state["nav_page"] == "⚡ Formula Cheat Sheets":
    st.title("⚡ High-Yield GATE Formula Cheat Sheets")
    st.caption("Quick revision reference for formulas tested every year.")
    st.write("")

    tab1, tab2, tab3 = st.tabs(["Probability & Statistics", "Linear Algebra", "Calculus & Optimization"])

    with tab1:
        st.markdown("""
        ### 📘 Probability & Distributions
        - **Total Probability Theorem:**  
          $$P(B) = \\sum_{i=1}^n P(B|A_i) P(A_i)$$
        - **Bayes' Rule:**  
          $$P(A_k|B) = \\frac{P(B|A_k) P(A_k)}{\\sum_{i} P(B|A_i) P(A_i)}$$
        - **Variance & Covariance:**  
          $$\\text{Var}(X) = E[X^2] - (E[X])^2, \\quad \\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$$
        - **Independence Condition:**  
          $$X \\perp Y \\implies E[XY] = E[X] E[Y] \\text{ and } \\text{Cov}(X, Y) = 0$$
        """)

    with tab2:
        st.markdown("""
        ### 📗 Linear Algebra & Matrix Calculus
        - **Rank-Nullity Theorem:**  
          $$\\text{Rank}(A) + \\text{Nullity}(A) = n \\quad (\\text{where } A \\text{ is } m \\times n)$$
        - **Subspace Dimension:**  
          $$\\dim(U + W) = \\dim(U) + \\dim(W) - \\dim(U \\cap W)$$
        - **Eigenvalues & Trace / Determinant:**  
          $$\\sum \\lambda_i = \\text{Trace}(A), \\quad \\prod \\lambda_i = \\det(A)$$
        - **Orthogonal Projection:**  
          $$\\pi_U(x) = B(B^T B)^{-1} B^T x$$
        """)

    with tab3:
        st.markdown("""
        ### 📙 Calculus & Optimization
        - **Gradient Vector:**  
          $$\\nabla f(x) = \\left[ \\frac{\\partial f}{\\partial x_1}, \\dots, \\frac{\\partial f}{\\partial x_d} \\right]^T$$
        - **Hessian Matrix & Convexity:**  
          $$H_{ij} = \\frac{\\partial^2 f}{\\partial x_i \\partial x_j}, \\quad H \\succeq 0 \\text{ (Positive semi-definite) } \\implies f \\text{ is convex}$$
        - **Gradient Descent Update:**  
          $$x^{(t+1)} = x^{(t)} - \\gamma \\nabla f(x^{(t)})$$
        """)
