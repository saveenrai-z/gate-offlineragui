import faiss
import json
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Optional
from config import VECTOR_DB_DIR
from modules.embeddings import EmbeddingManager

class VectorStore:
    def __init__(self, index_name: str = "gate_faiss", dimension: int = 384):
        self.index_name = index_name
        self.dimension = dimension
        self.index_path = VECTOR_DB_DIR / f"{index_name}.index"
        self.meta_path = VECTOR_DB_DIR / f"{index_name}_meta.json"
        self.index = None
        self.metadata = []
        self.embedding_mgr = EmbeddingManager()
        self._load_or_create()

    def _load_or_create(self):
        VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)
        if self.index_path.exists() and self.meta_path.exists():
            try:
                self.index = faiss.read_index(str(self.index_path))
                with open(self.meta_path, "r", encoding="utf-8") as f:
                    self.metadata = json.load(f)
                return
            except Exception as e:
                print(f"[VectorStore] Could not read existing index: {e}, creating new index.")
        self.index = faiss.IndexFlatIP(self.dimension)
        self.metadata = []

    def save(self):
        faiss.write_index(self.index, str(self.index_path))
        with open(self.meta_path, "w", encoding="utf-8") as f:
            json.dump(self.metadata, f, indent=2, ensure_ascii=False)

    def add_chunks(self, chunks: List[Dict[str, Any]], batch_size: int = 64):
        """Adds list of {'id':..., 'document':..., 'metadata':...} to index."""
        if not chunks:
            return

        texts = [c["document"] for c in chunks]
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i:i+batch_size]
            batch_chunks = chunks[i:i+batch_size]
            vectors = self.embedding_mgr.embed_texts(batch_texts)
            if self.index.d != vectors.shape[1]:
                # adjust dimension if needed
                self.dimension = vectors.shape[1]
                new_idx = faiss.IndexFlatIP(self.dimension)
                if self.index.ntotal > 0:
                    pass
                self.index = new_idx
            self.index.add(vectors)
            self.metadata.extend(batch_chunks)
        self.save()

    def search(self, query: str, top_k: int = 5, filter_subject: Optional[str] = None) -> List[Dict[str, Any]]:
        if self.index is None or self.index.ntotal == 0:
            return []

        query_vec = self.embedding_mgr.embed_query(query).reshape(1, -1)
        search_k = min(max(top_k * 5, 20), self.index.ntotal)
        scores, indices = self.index.search(query_vec, search_k)

        candidates = []
        for score, idx in zip(scores[0], indices[0]):
            if idx == -1 or idx >= len(self.metadata):
                continue
            item = self.metadata[idx]
            meta = item.get("metadata", {})
            candidates.append({
                "score": float(score),
                "text": item.get("document", ""),
                "id": item.get("id", ""),
                "metadata": meta
            })

        # If subject filter is specified, check if any match
        if filter_subject and filter_subject.lower() != "all subjects":
            filtered = [
                c for c in candidates 
                if filter_subject.lower() in c["metadata"].get("subject", "").lower()
                or filter_subject.lower() in c["text"].lower()
            ]
            if filtered:
                return filtered[:top_k]

        # Return best matching semantic chunks
        return candidates[:top_k]

    @property
    def total_vectors(self) -> int:
        return self.index.ntotal if self.index else 0
