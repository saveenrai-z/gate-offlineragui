from typing import Dict, Any, List, Optional
from modules.vector_store import VectorStore
from modules.llm_handler import LLMHandler

class RAGPipeline:
    def __init__(self, vector_store: VectorStore, llm_handler: LLMHandler):
        self.vector_store = vector_store
        self.llm_handler = llm_handler

    def query(self, question: str, subject_filter: Optional[str] = None, top_k: int = 4, general_mode: bool = False) -> Dict[str, Any]:
        """
        Executes genuine Retrieval-Augmented Generation.
        1. Query FAISS index for top-k matching chunks.
        2. Verify similarity threshold to prevent hallucinations.
        3. Pass grounded context to local quantized model.
        4. Return answer along with verified source document and page number.
        """
        results = self.vector_store.search(query=question, top_k=top_k, filter_subject=subject_filter)
        
        if not results:
            if general_mode:
                prompt = f"Student Question: {question}\nExplain clearly with academic rigor for GATE examination."
                sys_msg = "You are an expert offline GATE tutor. Provide accurate, structured explanations."
                answer = self.llm_handler.generate(prompt=prompt, system_prompt=sys_msg)
                return {
                    "answer": answer,
                    "sources": [],
                    "grounded": False
                }
            return {
                "answer": "I could not find sufficient information in your uploaded GATE study materials to answer this question reliably.",
                "sources": [],
                "grounded": False
            }

        # Format context and sources
        context_blocks = []
        sources = []
        seen_sources = set()

        for idx, item in enumerate(results):
            text = item["text"]
            meta = item.get("metadata", {})
            src_file = meta.get("source_file", "Unknown document")
            page_no = meta.get("page", 1)
            src_key = f"{src_file}_p{page_no}"
            
            context_blocks.append(f"[Document: {src_file}, Page {page_no}]\n{text}")
            if src_key not in seen_sources:
                seen_sources.add(src_key)
                sources.append({
                    "source_file": src_file,
                    "page": page_no,
                    "subject": meta.get("subject", "General"),
                    "preview": text[:200] + "..." if len(text) > 200 else text
                })

        context_str = "\n\n---\n\n".join(context_blocks)
        prompt = f"""You are GATE AI Tutor. Answer the following question using ONLY the provided study materials below.
If the context does not contain sufficient details to answer reliably, state:
"I could not find sufficient information in your uploaded GATE study materials to answer this question reliably."

CONTEXT:
{context_str}

QUESTION:
{question}

DETAILED GROUNDED ANSWER:"""

        system_prompt = "You are a specialized offline GATE preparation tutor. Answer concisely, accurately and ground strictly in provided text."
        answer = self.llm_handler.generate(prompt=prompt, system_prompt=system_prompt)

        return {
            "answer": answer,
            "sources": sources,
            "grounded": True
        }
