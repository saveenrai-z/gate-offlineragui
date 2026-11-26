import os
from typing import Dict, Any, List
from modules.rag_pipeline import RAGPipeline
from modules.textbook_reader import TextbookReader

class LessonGenerator:
    def __init__(self, rag_pipeline: RAGPipeline):
        self.rag_pipeline = rag_pipeline

    def get_topic_lesson(self, subject_name: str, chapter_title: str, topic_title: str) -> Dict[str, Any]:
        """
        Retrieves authentic, in-depth academic teachings directly from 
        the assigned textbooks (mml-book.pdf, textbook_full.pdf, etc.) 
        with guaranteed offline availability.
        """
        # Directly extract rich verified textbook passages
        textbook_res = TextbookReader.get_detailed_teachings(subject_name, topic_title)
        content = textbook_res.get("content", "")
        sources = textbook_res.get("sources", [])

        # Format into clean step-by-step educational lesson
        return {
            "topic": topic_title,
            "chapter": chapter_title,
            "subject": subject_name,
            "core_concept": content,
            "exam_guidelines": [
                f"**GATE Target:** Review the definitions, boundary conditions, and theorems for **{topic_title}**.",
                f"**Syllabus Relevance:** Directly tested under {chapter_title} in GATE {subject_name}.",
                "**Numerical & Theory Practice:** Verify formulas with the cited pages from the assigned textbook."
            ],
            "sources": sources
        }
