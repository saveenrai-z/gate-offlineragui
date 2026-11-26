from typing import List, Dict, Any

class DocumentChunker:
    def __init__(self, chunk_size: int = 700, chunk_overlap: int = 120):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_pages(self, pages: List[Dict[str, Any]], gate_paper: str = "GATE-DA", subject: str = "General", doc_type: str = "material") -> List[Dict[str, Any]]:
        """
        Chunks text from a list of page dictionaries while preserving rich metadata.
        """
        chunks = []
        for p in pages:
            text = p.get("text", "")
            page_no = p.get("page_number", 1)
            file_name = p.get("file_name", "")
            
            if len(text) <= self.chunk_size:
                if len(text.strip()) > 20: # ignore trivial noise
                    chunks.append({
                        "id": f"{file_name}_p{page_no}_c0",
                        "document": text,
                        "metadata": {
                            "gate_paper": gate_paper,
                            "subject": subject,
                            "doc_type": doc_type,
                            "source_file": file_name,
                            "page": page_no
                        }
                    })
            else:
                start = 0
                c_idx = 0
                step = self.chunk_size - self.chunk_overlap
                while start < len(text):
                    end = start + self.chunk_size
                    chunk_text = text[start:end]
                    if len(chunk_text.strip()) > 30:
                        chunks.append({
                            "id": f"{file_name}_p{page_no}_c{c_idx}",
                            "document": chunk_text,
                            "metadata": {
                                "gate_paper": gate_paper,
                                "subject": subject,
                                "doc_type": doc_type,
                                "source_file": file_name,
                                "page": page_no
                            }
                        })
                    start += step
                    c_idx += 1
        return chunks
