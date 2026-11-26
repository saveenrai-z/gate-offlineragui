from typing import Dict, Any, List
from modules.rag_pipeline import RAGPipeline

class RevisionManager:
    def __init__(self, rag_pipeline: RAGPipeline):
        self.rag_pipeline = rag_pipeline

    def get_revision_summary(self, subject: str, chapter: str) -> Dict[str, Any]:
        """
        Synthesizes high-yield revision cards and cheat-sheets from syllabus materials.
        """
        query = f"{subject} {chapter} revision summary formulas key definitions exam tips"
        rag_res = self.rag_pipeline.query(question=query, subject_filter=subject, top_k=4, general_mode=True)
        content = rag_res.get("answer", "")

        return {
            "subject": subject,
            "chapter": chapter,
            "cheat_sheet": content,
            "high_yield_points": [
                f"Frequently tested theorems in {chapter}",
                f"Edge case handling for standard GATE numerical problems",
                f"Time-saving shortcuts and formula variations"
            ],
            "sources": rag_res.get("sources", [])
        }
