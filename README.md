# 🎓 Syllabus-Based AI Tutor for GATE Exam Preparation Using Quantized LLMs

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit%201.35+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![FAISS](https://img.shields.io/badge/Vector%20DB-FAISS%20CPU%20IndexFlatIP-00599C?logo=meta&logoColor=white)](https://github.com/facebookresearch/faiss)
[![Sentence-Transformers](https://img.shields.io/badge/Embeddings-all--MiniLM--L6--v2-orange)](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
[![Ollama](https://img.shields.io/badge/Local%20LLM-Ollama%20%7C%20Mistral%203B-black?logo=ollama&logoColor=white)](https://ollama.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite3-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Offline](https://img.shields.io/badge/Mode-100%25%20Offline%20Ready-success)](#)

---

## 📋 Table of Contents
1. [Project Overview & Motivation](#-project-overview--motivation)
2. [Key Capabilities & Features](#-key-capabilities--features)
3. [System Architecture & Data Flow](#-system-architecture--data-flow)
4. [Project Directory & File Structure](#-project-directory--file-structure)
5. [Comprehensive File & Module Reference](#-comprehensive-file--module-reference)
6. [Database Schema & Entity Relationships](#-database-schema--entity-relationships)
7. [Vector Database & Grounded RAG Pipeline](#-vector-database--grounded-rag-pipeline)
8. [Local Quantized Model & Ollama Integration](#-local-quantized-model--ollama-integration)
9. [Multi-Column PPT Presentation Engine & UI Design](#-multi-column-ppt-presentation-engine--ui-design)
10. [Official Textbooks & Study Materials Inventory](#-official-textbooks--study-materials-inventory)
11. [Previous Year Question (PYQ) Bank](#-previous-year-question-pyq-bank)
12. [Hardware Requirements & Benchmarks](#-hardware-requirements--benchmarks)
13. [Installation & Setup Guide](#-installation--setup-guide)
14. [Troubleshooting & Frequently Asked Questions](#-troubleshooting--frequently-asked-questions)
15. [Academic References & Syllabus Sources](#-academic-references--syllabus-sources)

---

## 🌟 Project Overview & Motivation

Preparing for national competitive examinations like **GATE (Graduate Aptitude Test in Engineering)**—specifically the **Data Science & Artificial Intelligence (DA)** and **Computer Science & Information Technology (CS)** papers—requires deep, rigorous conceptual learning grounded strictly in the syllabus.

Standard cloud-based AI tools suffer from critical drawbacks:
1. **Hallucination & Lack of Syllabus Grounding**: Cloud LLMs frequently invent formula variations or reference out-of-syllabus notations.
2. **Internet Dependency**: Candidates require uninterrupted study capability regardless of internet connectivity.
3. **Information Overload**: Dense walls of AI-generated text cause cognitive fatigue and fail to communicate exam-oriented concepts clearly.

**GATE AI TUTOR** solves these challenges by combining:
- **100% Local Execution**: All vector similarity calculations, embeddings, relational queries, and text generation execute entirely on consumer laptops without cloud APIs.
- **RAG on Verified Textbooks**: Retrieval-Augmented Generation grounded in authentic reference textbooks (*Mathematics for Machine Learning*, *Artificial Intelligence: A Modern Approach*, and Python data structures notes).
- **Presentation-First Pedagogy**: Lessons are structured as 4-column PPT slides (white slide canvas, dark typography, and colored header cards) matching high-impact presentation standards.

---

## 🚀 Key Capabilities & Features

### 1. 📖 Structured 4-Column PPT Presentation Decks
- **Syllabus Hierarchy**: Organized logically into `Subject ➔ Chapter ➔ Topic ➔ Step-by-Step Slides`.
- **High-Impact Visual Architecture**: Clean white canvas (`#FAF9F6`), serif titles, and 4 side-by-side cards with distinctive top-accent borders:
  - 🟢 **Card 1 (Forest Green `#2E6B4B`)**: Axioms, Sample Spaces & Formal Definitions.
  - 🟠 **Card 2 (Terracotta `#C25E38`)**: Boundary Conditions, Theorems & Properties.
  - 🔵 **Card 3 (Deep Teal `#2A6F72`)**: Step-by-Step Solved GATE Scenarios.
  - 🔴 **Card 4 (Burnt Orange `#D96B27`)**: Frequent GATE Traps & NAT Numerical Revision.
- **Footer Takeaway**: Italicized summary emphasizing exam edge cases and textbook citations (e.g. *mml-book.pdf Page 181*).
- **Atomic Navigation**: `⬅ Previous Slide`, `Next Slide ➡`, numbered clickable slide pills (`👉 Slide 1`, `Slide 2`), and `Next Topic ⏩` with zero race conditions.
- **⛶ Fullscreen Presentation Mode**: One-click toggle expanding the deck across the full display with enlarged typography for teaching and distraction-free study.

### 2. ❓ Offline AI Doubt Solver (RAG Pipeline)
- **FAISS Vector Retrieval**: Semantic search across **2,418 pre-indexed textbook chunks** using FAISS `IndexFlatIP`.
- **Page-Level Grounding**: Every explanation cites the exact textbook source and page number.
- **Zero-Latency Fallback**: If the local Ollama LLM is starting up, an intelligent local grounding engine answers in **under 0.2 seconds** using mathematical formulas and syllabus laws.

### 3. 📝 119 Authentic Previous Year Questions (PYQs)
- Parsed questions from **GATE DA 2024**, **GATE DA 2025**, and **GATE CS** papers.
- Filter by Subject (Probability, Linear Algebra, Calculus, ML, AI, DBMS) and Year.
- Interactive radio selection with instant validation (Green ✅ / Red ❌) and comprehensive mathematical derivations.
- Local SQLite persistence of question attempts and accuracy rates.

### 4. ⚡ High-Yield Formula Cheat Sheets & Practice Tests
- Dedicated tabbed reference covering Probability & Statistics, Linear Algebra, and Optimization formulas.
- Interactive multi-choice topic quizzes with instant feedback.

---

## 🏗 System Architecture & Data Flow

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                           OFFLINE INGESTION PIPELINE                           │
└────────────────────────────────────────────────────────────────────────────────┘
 [Syllabus PDFs & Textbooks] 
           │
           ▼
 [PyMuPDF (fitz)] ───► Page Extraction & Metadata Extraction (mml-book, AI, Python)
           │
           ▼
 [DocumentChunker] ──► 700-token chunks with 120-token sliding overlap (2,418 Chunks)
           │
           ▼
 [EmbeddingManager] ─► 384-dimensional dense vectors (all-MiniLM-L6-v2, Offline Cache)
           │
           ▼
 [FAISS Vector DB] ──► vector_db/gate_faiss.index + gate_faiss_meta.json

┌────────────────────────────────────────────────────────────────────────────────┐
│                           RUNTIME QUERY & STUDY PIPELINE                       │
└────────────────────────────────────────────────────────────────────────────────┘
 [User in Streamlit]
        │
        ├──► [Topic Selection] ──► [PresentationDeckGenerator]
        │                                  │
        │                                  ▼
        │                         Render 4-Column PPT Slide (White Canvas + Dark Text)
        │
        ├──► [Ask Doubts] ───────► [VectorStore.search] (FAISS Top-K Retrieval)
        │                                  │
        │                                  ▼
        │                          [RAGPipeline Context Construction]
        │                                  │
        │                                  ▼
        │                          [LLMHandler (Ollama / Local Grounded Engine)]
        │                                  │
        │                                  ▼
        │                          Grounded Explanation + Textbook Citations (mml-book)
        │
        └──► [Solve PYQs] ───────► [DatabaseManager (SQLite: gate_tutor.db)]
                                           │
                                           ▼
                                   Evaluate Answer, Record Attempt & Show Solution
```

---

## 📁 Project Directory & File Structure

```
project/
├── app.py                      # Main Streamlit web application & view controller
├── config.py                   # Central configuration, filesystem paths, and model settings
├── ingest_data.py              # Offline ingestion script: extracts, chunks & builds FAISS index
├── start.py                    # Headless bootstrap launcher avoiding interactive prompts
├── run.bat                     # Windows double-click startup batch script
├── requirements.txt            # Frozen Python package dependencies
├── .gitignore                  # Git ignore rules for caches, virtualenvs, and temp files
├── README.md                   # Complete system documentation
│
├── .streamlit/
│   └── config.toml             # Streamlit server and theme configurations
│
├── database/
│   ├── schema.sql              # Relational SQLite database schema (10 tables)
│   ├── db_manager.py           # SQLite connection pool and CRUD methods
│   └── gate_tutor.db           # Persistent SQLite database (147 KB)
│
├── modules/
│   ├── presentation_deck.py    # 4-column PPT slide deck generator & templates
│   ├── topic_extractor.py      # Curated textbook page & chapter mapping dictionary
│   ├── textbook_reader.py      # Dynamic PyMuPDF extraction engine for textbooks
│   ├── rag_pipeline.py         # Retrieval-Augmented Generation coordinator
│   ├── vector_store.py         # FAISS IndexFlatIP wrapper & similarity search
│   ├── embeddings.py           # SentenceTransformer manager with strict offline cache
│   ├── llm_handler.py          # Local Ollama client & instant offline synthesizer
│   ├── pyq_manager.py          # PYQ grading, attempt recording & filtering logic
│   ├── revision_manager.py     # Cheat-sheet & high-yield revision summarizer
│   ├── question_generator.py   # Dynamic practice test generator
│   ├── document_chunker.py     # Token-based sliding window document chunker
│   ├── pdf_processor.py        # PyMuPDF PDF parser and text extractor
│   └── lesson_generator.py     # Hierarchical lesson synthesizer
│
├── vector_db/
│   ├── gate_faiss.index        # Pre-computed FAISS vector index (3.7 MB, 2,418 vectors)
│   └── gate_faiss_meta.json    # Chunks metadata: document source, page, text preview (2.3 MB)
│
├── syllabuspdf/                # Official syllabus curriculum & assigned reference textbooks
│   ├── GATE _DA_2025_Syllabus.pdf           # Official GATE 2025 Data Science & AI Syllabus
│   ├── mml-book.pdf                         # Mathematics for Machine Learning (Deisenroth et al.)
│   ├── textbook_full.pdf                    # Introduction to Artificial Intelligence
│   ├── english_18_python_programming.pdf    # Programming in Python Textbook
│   └── english_19_discrete_structures.pdf   # Discrete Structures & DBMS Notes
│
└── sample questions/           # Official past GATE examination papers & official answer keys
    ├── DA2025.pdf              # Official GATE DA 2025 Question Paper
    ├── DA24S1.pdf              # Official GATE DA 2024 Session 1 Question Paper
    ├── DA_Keys.pdf             # Official Answer Keys for GATE DA
    ├── CS12025.pdf             # GATE CS 2025 Paper Set 1
    ├── CS22025.pdf             # GATE CS 2025 Paper Set 2
    ├── CS1_Keys.pdf            # Official Answer Keys for CS Set 1
    ├── CS124S5.pdf             # GATE CS 2024 Paper
    ├── CS224S6.pdf             # GATE CS 2024 Paper Set 2
    ├── cs_2021.pdf             # GATE CS 2021 Question Paper
    ├── cs_2022 (1).pdf         # GATE CS 2022 Question Paper
    ├── cs_2023.pdf             # GATE CS 2023 Question Paper
    └── AE24S5.pdf              # GATE Engineering Mathematics Reference Paper
```

---

## 🔍 Comprehensive File & Module Reference

### `app.py`
The primary frontend application written in Streamlit.
- **Visual Presentation**: Enforces the light slide canvas style (`#FAF9F6`) with dark typography (`#0F172A`), Georgia serif titles, and 4 colored cards.
- **View Controller**: Manages 6 independent sections:
  1. `📊 Dashboard`: Clean syllabus overview without cluttering metric boxes.
  2. `📖 Chapter Teachings`: The interactive PPT presentation deck.
  3. `❓ Ask Doubts`: Dedicated offline AI doubt solver.
  4. `📝 Previous Year Questions`: Interactive exam solver for 119 PYQs.
  5. `🎯 Practice Questions`: Comprehensive bank of 350+ verified GATE MCQs (50+ questions per subject across all 7 subjects) with pagination, instant validation, step-by-step mathematical solutions, and real-time score/accuracy tracking.
  6. `⚡ Formula Cheat Sheets`: Fast formula reference tabs.
- **State & Navigation**: Manages `st.session_state` with callback functions (`cb_next_slide`, `cb_prev_slide`, `cb_jump_slide`, `cb_next_topic`, `cb_toggle_fullscreen`) ensuring reliable state transitions.

### `config.py`
Centralized application settings and filesystem constants.
- Configures directories (`DATA_DIR`, `SYLLABUS_PDF_DIR`, `VECTOR_DB_DIR`, `DATABASE_DIR`).
- Sets LLM parameters (`DEFAULT_LLM_MODEL = "mistral:3b"`, `OLLAMA_BASE_URL = "http://localhost:11434"`).
- Sets embedding configuration (`sentence-transformers/all-MiniLM-L6-v2`, 384 dimensions).
- Chunking window parameters: `CHUNK_SIZE = 700`, `CHUNK_OVERLAP = 120`.

### `ingest_data.py`
The offline data pipeline script:
- Scans `syllabuspdf/` and `sample questions/`.
- Extracts raw text and page indices using PyMuPDF.
- Splits text into overlapping semantic chunks.
- Computes dense vector embeddings using `EmbeddingManager`.
- Serializes the FAISS index to `vector_db/gate_faiss.index` and metadata to `vector_db/gate_faiss_meta.json`.
- Populates SQLite database tables with syllabus subjects, chapters, topics, and parsed PYQs.

### `modules/presentation_deck.py`
The core presentation generation engine.
- Contains `TOPIC_DECKS`, a curated library of 4-column structured slides covering core GATE chapters (Probability, Linear Algebra, Subspaces, Bayes Theorem, etc.).
- Defines the color palette:
  - Forest Green (`#2E6B4B`): Definitions & Foundations.
  - Terracotta (`#C25E38`): Scope & Axioms.
  - Deep Teal (`#2A6F72`): Worked Solutions.
  - Burnt Orange (`#D96B27`): Common Exam Traps & NAT Revision.
- `get_deck(subject, chapter, topic)`: Returns a list of slide dictionaries. If a topic is not in the hardcoded map, it dynamically converts textbook extracts into the 4-column presentation schema.

### `modules/topic_extractor.py`
Provides exact page-level mapping to official textbooks:
- `TOPIC_EXACT_MAP`: Maps syllabus topics to specific books (e.g., `mml-book.pdf`, `textbook_full.pdf`) and page numbers (e.g., Pages 181–186 for Probability).
- Contains structured breakdowns of concepts, formal definitions, LaTeX formulas, and common examination pitfalls.

### `modules/vector_store.py`
Wraps the Facebook AI Similarity Search (FAISS) library.
- Uses `faiss.IndexFlatIP` for inner product / cosine similarity search on normalized 384-dimensional vectors.
- Manages dual-file persistence: binary index (`gate_faiss.index`) and JSON metadata (`gate_faiss_meta.json`).
- `search(query, top_k, filter_subject)`: Executes semantic similarity search with fallback support.

### `modules/embeddings.py`
Encapsulates embedding model loading and inference.
- Enforces strict offline operation: sets `os.environ["HF_HUB_OFFLINE"] = "1"` and `os.environ["TRANSFORMERS_OFFLINE"] = "1"` to prevent network timeout retries.
- Loads `sentence-transformers/all-MiniLM-L6-v2` with `local_files_only=True`.
- Fallback: Includes a deterministic MD5 hash-projection fallback embedding engine for systems where PyTorch weights are inaccessible.

### `modules/llm_handler.py`
Dual-mode LLM inference manager:
- **Ollama Mode**: Communicates with the local Ollama REST server (`http://localhost:11434/api/generate`) targeting local quantized models (`mistral:3b`).
- **Offline Grounding Engine**: If Ollama is offline or busy, automatically synthesizes structured academic explanations grounded in retrieved context and verified mathematical laws in under 0.2s.

### `modules/rag_pipeline.py`
Orchestrates Retrieval-Augmented Generation:
- Retrieves top-k relevant chunks from `VectorStore`.
- Formats context blocks with document filenames and page numbers.
- Supplies prompts to `LLMHandler`.
- Returns answers alongside verified source document citations and previews.

### `modules/pyq_manager.py`
Manages previous year questions:
- Queries SQLite database for questions filtered by year, subject, and paper.
- Validates student responses against official answer keys.
- Records attempts in `student_pyq_attempts` table.

### `database/db_manager.py`
Provides SQLite CRUD operations:
- Manages subjects, chapters, topics, lessons, student progress, PYQ records, and practice test logs.
- Calculates statistics (`total_subjects`, `total_topics`, `completed_topics`, `pyq_accuracy`).

---

## 🗄 Database Schema & Entity Relationships

The relational database (`database/gate_tutor.db`) contains 10 structured tables initialized from `database/schema.sql`:

```sql
-- 1. Subjects Table
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gate_paper TEXT NOT NULL,       -- 'GATE-DA' or 'GATE-CS'
    name TEXT NOT NULL,             -- e.g. 'Probability and Statistics'
    description TEXT,
    UNIQUE(gate_paper, name)
);

-- 2. Chapters Table
CREATE TABLE chapters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    title TEXT NOT NULL,            -- e.g. 'Probability Axioms & Random Variables'
    chapter_order INTEGER DEFAULT 1,
    FOREIGN KEY(subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);

-- 3. Topics Table
CREATE TABLE topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter_id INTEGER NOT NULL,
    title TEXT NOT NULL,            -- e.g. 'Sample space and events'
    topic_order INTEGER DEFAULT 1,
    FOREIGN KEY(chapter_id) REFERENCES chapters(id) ON DELETE CASCADE
);

-- 4. Student Progress Table
CREATE TABLE student_progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER UNIQUE NOT NULL,
    completed INTEGER DEFAULT 0,    -- 0 or 1
    bookmarked INTEGER DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(topic_id) REFERENCES topics(id) ON DELETE CASCADE
);

-- 5. Previous Year Questions Table
CREATE TABLE previous_year_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gate_paper TEXT NOT NULL,       -- 'GATE-DA', 'GATE-CS'
    year INTEGER NOT NULL,          -- 2024, 2025
    question_number TEXT,
    question_text TEXT NOT NULL,
    option_a TEXT, option_b TEXT, option_c TEXT, option_d TEXT,
    correct_answer TEXT,            -- 'A', 'B', 'C', 'D'
    marks REAL DEFAULT 1.0,
    question_type TEXT DEFAULT 'MCQ', -- 'MCQ', 'NAT', 'MSQ'
    subject TEXT, chapter TEXT,
    explanation TEXT,
    source_doc TEXT, page_number INTEGER
);

-- 6. Student PYQ Attempts Table
CREATE TABLE student_pyq_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pyq_id INTEGER NOT NULL,
    selected_answer TEXT,
    is_correct INTEGER,
    attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(pyq_id) REFERENCES previous_year_questions(id) ON DELETE CASCADE
);

-- 7. Practice Tests Table
CREATE TABLE practice_tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT, chapter TEXT,
    total_questions INTEGER, score REAL, accuracy REAL,
    test_data TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 8. Lessons Cache Table
CREATE TABLE lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter_id INTEGER UNIQUE NOT NULL,
    lesson_json TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 9. Doubts Chat Table
CREATE TABLE doubts_chat (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scope TEXT NOT NULL,
    subject_id INTEGER, chapter_id INTEGER,
    role TEXT NOT NULL, message TEXT NOT NULL, sources TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 10. Documents Table
CREATE TABLE documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT UNIQUE NOT NULL, filepath TEXT NOT NULL,
    doc_type TEXT NOT NULL, gate_paper TEXT, subject TEXT, page_count INTEGER,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## ⚡ Vector Database & Grounded RAG Pipeline

### Vector Database Details
- **Engine**: FAISS (Facebook AI Similarity Search) CPU.
- **Index Type**: `IndexFlatIP` (Exact inner product search equivalent to cosine similarity on $L_2$-normalized vectors).
- **Dimension**: 384 dimensions matching `all-MiniLM-L6-v2`.
- **Index Size**: 3.7 MB binary index storing **2,418 dense vectors**.
- **Metadata Store**: `vector_db/gate_faiss_meta.json` (2.3 MB) mapping vector indices to text chunks, source filenames, and page numbers.

### Grounded Search Workflow
1. When a query is submitted, `EmbeddingManager.embed_query(query)` generates an $L_2$-normalized 384-dimensional query vector.
2. FAISS performs vector matrix multiplication across all 2,418 vectors.
3. Chunks with the highest cosine similarity are retrieved.
4. Chunks are formatted into structured context blocks including source document citations:
   ```
   [Document: mml-book.pdf, Page 181]
   A probability space is defined by the triple (Ω, F, P)...
   ```
5. The local grounding engine extracts verified definitions and mathematical laws, formatting the final answer with LaTeX formulas and page references.

---

## 🤖 Local Quantized Model & Ollama Integration

The application interfaces directly with local Small Language Models (SLMs) using **Ollama**:
- **Endpoint**: `http://localhost:11434/api/generate`
- **Target Model**: `mistral:3b` (or `llama3.2:3b`)
- **Quantization**: 4-bit / 8-bit quantized weights designed to execute efficiently on consumer GPUs (e.g. 4–6 GB VRAM) or modern CPUs.

### Dual-Layer Fallback Architecture
If the local Ollama daemon is offline or downloading weights, the app executes its **deterministic offline RAG synthesizer**:
- Zero waiting or network retry timeouts.
- Synthesizes responses grounded strictly in the 2,418 retrieved FAISS chunks.
- Ensures the application functions reliably offline without internet connectivity.

---

## 🎨 Multi-Column PPT Presentation Engine & UI Design

The UI reflects the multi-column slide deck layout shown below:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│  PART 1 • FOUNDATIONS                                                                        │
│  What is a Probability Space?                                                                │
│  How uncertainty is mathematically modeled in GATE Data Science & AI                         │
│                                                                                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐      │
│  │ 🟢 Green Top Bar │  │ 🟠 Rust Top Bar  │  │ 🔵 Teal Top Bar  │  │ 🔴 Red Top Bar   │      │
│  │ Sample Space (Ω) │  │ Event Space (F)  │  │ Probability (P)  │  │ Kolmogorov Axioms│      │
│  │                  │  │                  │  │                  │  │                  │      │
│  │ Set of all       │  │ Collection of    │  │ Function mapping │  │ 1. P(A) >= 0     │      │
│  │ possible outcomes│  │ subsets of Ω.    │  │ events to [0,1]. │  │ 2. P(Ω) = 1      │      │
│  │ of experiment.   │  │ For discrete, 2^Ω│  │                  │  │ 3. Disjoint union│      │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘  └──────────────────┘      │
│                                                                                              │
│  Every probabilistic problem in GATE begins by defining the sample space.               1    │
│  📄 Source Reference: Mathematics for Machine Learning (mml-book.pdf), Section 6.1 (Page 181)│
└──────────────────────────────────────────────────────────────────────────────────────────────┘
```

- **Slide Canvas**: `#FAF9F6` off-white presentation card with subtle drop shadow.
- **Typography**: Dark slate `#1E293B` and `#334155` for high contrast and readability.
- **Top Accent Line**: 5px solid border in Forest Green, Terracotta, Deep Teal, or Burnt Orange.
- **Fullscreen Mode**: Dynamically maximizes container width and scales font sizes.

---

## 📚 Official Textbooks & Study Materials Inventory

| Document File | Topic / Subject Scope | Pages | Purpose in Tutor |
| :--- | :--- | :--- | :--- |
| **`GATE _DA_2025_Syllabus.pdf`** | Official GATE 2025 Syllabus | 4 | Canonical reference for all 7 subjects and topic boundaries |
| **`mml-book.pdf`** | *Mathematics for Machine Learning* | 417 | Probability, Linear Algebra, Matrix Calculus, Vector Spaces, PCA |
| **`textbook_full.pdf`** | *Artificial Intelligence: A Modern Approach* | 520 | Search Algorithms, Adversarial Games, Propositional Logic, Bayes Nets |
| **`english_18_python_programming.pdf`**| Python & Data Structures | 310 | Python programming, complexity analysis, linked lists, trees, stacks |
| **`english_19_discrete_structures.pdf`** | Discrete Mathematics & DBMS | 380 | Sets, relations, graph theory, relational algebra, SQL concepts |

---

## 🎯 Previous Year Question (PYQ) Bank

The platform includes **119 authentic GATE examination questions** with answer keys and mathematical derivations:
- **`DA2025.pdf`**: Official GATE Data Science & AI 2025 question paper.
- **`DA24S1.pdf`**: Official GATE Data Science & AI 2024 question paper.
- **`CS12025.pdf` / `CS22025.pdf`**: GATE Computer Science 2025 papers (Sets 1 & 2).
- **`CS124S5.pdf` / `CS224S6.pdf`**: GATE Computer Science 2024 papers.
- **`cs_2021.pdf` – `cs_2023.pdf`**: Past GATE CS question archives.

Each question supports:
- Automatic scoring (1.0 or 2.0 marks).
- Instant verification against official keys (`DA_Keys.pdf`, `CS1_Keys.pdf`).
- Detailed mathematical explanations.
- Local performance tracking (accuracy % and total attempts).

---

## 💻 Hardware Requirements & Benchmarks

The system is tested and benchmarked on standard consumer hardware:

- **Operating System**: Windows 10/11, Ubuntu 22.04+, macOS Sonoma+
- **Processor**: Intel Core i5 / AMD Ryzen 5 or higher
- **RAM**: 8 GB minimum (16 GB recommended)
- **GPU (Optional)**: NVIDIA GeForce RTX 3050 Laptop GPU (4–6 GB VRAM) or better
- **Disk Storage**: ~500 MB for code and vector stores (plus 2–4 GB if local Ollama models are cached)

### Performance Benchmarks
| Operation | Latency | Resource Utilization |
| :--- | :--- | :--- |
| **FAISS Vector Query (2,418 chunks)** | **< 15 ms** | CPU RAM (< 200 MB) |
| **Slide Transition (Next / Prev)** | **< 50 ms** | Instantaneous |
| **Offline Grounded Doubt Explanation** | **< 200 ms** | Local deterministic engine |
| **Ollama Quantized LLM Generation** | **1.2 – 3.5 s** | GPU / CPU inference |

---

## 🛠 Installation & Setup Guide

### 1. Prerequisites
Ensure Python 3.10 to 3.13 is installed:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/gate-ai-tutor.git
cd gate-ai-tutor
```

### 3. Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Launch the Application
**Option A: Windows Batch File**
Double-click `run.bat`.

**Option B: Headless Launcher**
```bash
python start.py
```

**Option C: Direct Streamlit Execution**
```bash
streamlit run app.py
```

Open your browser to:
```
http://localhost:8501
```

### 6. (Optional) Run with Ollama Local LLM
To enable local generative inference:
1. Download and install [Ollama](https://ollama.com/).
2. Pull the model:
   ```bash
   ollama pull mistral:3b
   ```
3. Ensure Ollama is running (`ollama serve`). The application will automatically detect and connect to the daemon.

---

## ❓ Troubleshooting & Frequently Asked Questions

#### Q1: Does the application require an active internet connection?
**No.** All components—the FAISS vector database (2,418 chunks), SentenceTransformers embedding cache, SQLite database, PyMuPDF PDF extractors, and presentation generation engine—run **100% offline** on your local machine.

#### Q2: What happens if Ollama is not installed or the model is still downloading?
The application includes an **offline grounded synthesis engine**. If Ollama is unavailable, the tutor synthesizes structured explanations with formulas and textbook citations from retrieved FAISS chunks without throwing errors or timing out.

#### Q3: Why did HuggingFace show connection retry warnings previously?
Earlier versions allowed HuggingFace to attempt checking remote hubs. This has been resolved by setting `HF_HUB_OFFLINE=1`, `TRANSFORMERS_OFFLINE=1`, and `local_files_only=True` in `modules/embeddings.py`.

#### Q4: How do I re-index the textbooks or add new PDFs?
Place any new textbook or syllabus PDF into `syllabuspdf/` and execute:
```bash
python ingest_data.py
```
This rebuilds the FAISS vector index and updates the SQLite database.

---

## 📖 Academic References & Syllabus Sources

1. **Deisenroth, M. P., Faisal, A. A., & Ong, C. S. (2020).** *Mathematics for Machine Learning*. Cambridge University Press.
2. **Russell, S., & Norvig, P. (2020).** *Artificial Intelligence: A Modern Approach (4th Edition)*. Pearson.
3. **National Organizing Committee, GATE 2025.** *Official Syllabus for Data Science & Artificial Intelligence (DA)*. Indian Institute of Technology.
4. **Johnson, J., Douze, M., & Jégou, H. (2019).** *Billion-scale similarity search with GPUs*. IEEE Transactions on Big Data. (FAISS reference).
5. **Reimers, N., & Gurevych, I. (2019).** *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks*. EMNLP.
