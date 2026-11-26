import re
from typing import List, Dict, Any
from modules.textbook_reader import TextbookReader

class SlideLessonGenerator:
    """
    Transforms syllabus topics and authentic textbook passages into 
    clean, high-impact presentation slides (PPT style):
    Slide 1: Core Definition & Concept
    Slide 2: Mathematical Formulations & Axioms
    Slide 3: Real Example / Problem
    Slide 4: GATE Exam Traps & Key Takeaways
    """

    @classmethod
    def get_topic_slides(cls, subject_name: str, chapter_title: str, topic_title: str) -> List[Dict[str, Any]]:
        raw_data = TextbookReader.get_detailed_teachings(subject_name, topic_title)
        raw_text = raw_data.get("content", "")
        sources = raw_data.get("sources", [])
        src_note = f"📄 {sources[0]['source_file']} (Page {sources[0]['page']})" if sources else "Official Syllabus"

        # Split into readable sentences/paragraphs
        sentences = [s.strip() for s in re.split(r'\. |\n', raw_text) if len(s.strip()) > 25]

        # Slide 1: Concept & Definition
        p1 = " ".join(sentences[:3]) if len(sentences) >= 3 else f"Fundamental principles of {topic_title} for GATE {subject_name}."
        slide_1 = {
            "slide_num": 1,
            "title": f"📌 Core Concept: {topic_title}",
            "subtitle": f"{subject_name} • {chapter_title}",
            "points": [
                f"**Topic Goal:** Master the foundational theory of **{topic_title}**.",
                f"**Definition:** {p1}",
                f"**Relevance:** Tested extensively in multiple-choice (MCQ) and numerical (NAT) GATE questions."
            ],
            "source": src_note
        }

        # Slide 2: Mathematical Formulation
        p2 = " ".join(sentences[3:6]) if len(sentences) >= 6 else "Key mathematical conditions and properties as derived in syllabus textbooks."
        slide_2 = {
            "slide_num": 2,
            "title": f"⚡ Mathematical Formulations & Properties",
            "subtitle": f"{topic_title} Properties",
            "points": [
                f"**Theoretical Axioms:** {p2}",
                "**Boundary Conditions:** Check non-negativity, normalization, and closed-domain invariants.",
                "**Standard Notation:** Ensure dimensional consistency when applying formulas."
            ],
            "source": src_note
        }

        # Slide 3: Worked Example / Application
        p3 = " ".join(sentences[6:9]) if len(sentences) >= 9 else f"Standard scenario illustrating {topic_title} in practice."
        slide_3 = {
            "slide_num": 3,
            "title": f"💡 Step-by-Step Example Scenario",
            "subtitle": "Conceptual Walkthrough",
            "points": [
                f"**Example Scenario:** {p3}",
                "**Step 1:** Identify known variables and constraints given in the problem statement.",
                "**Step 2:** Apply the fundamental theorem/formula verified above.",
                "**Step 3:** Double-check whether edge conditions or constraints alter the final result."
            ],
            "source": src_note
        }

        # Slide 4: GATE Exam Traps & High-Yield Summary
        slide_4 = {
            "slide_num": 4,
            "title": f"🎯 GATE Exam Traps & High-Yield Revision",
            "subtitle": "Key Takeaways for Students",
            "points": [
                f"**Common Trap 1:** Misinterpreting discrete vs. continuous boundary assumptions in {topic_title}.",
                "**Common Trap 2:** Calculation errors when computing normalization constants or matrix ranks.",
                "**Quick Revision:** Remember the core invariance properties before solving numerical answer type (NAT) problems."
            ],
            "source": src_note
        }

        return [slide_1, slide_2, slide_3, slide_4]
