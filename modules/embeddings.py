import os
import numpy as np
from typing import List, Union

# Enforce strict offline operation for HuggingFace & SentenceTransformers
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

class EmbeddingManager:
    _instance = None
    _model = None

    def __new__(cls, model_name: str = "all-MiniLM-L6-v2"):
        if cls._instance is None:
            cls._instance = super(EmbeddingManager, cls).__new__(cls)
            cls._instance.model_name = model_name
        return cls._instance

    def load_model(self):
        if self._model is None:
            try:
                from sentence_transformers import SentenceTransformer
                # Use local_files_only=True to prevent any network latency or timeout
                self._model = SentenceTransformer(self.model_name, local_files_only=True)
            except Exception:
                try:
                    from sentence_transformers import SentenceTransformer
                    self._model = SentenceTransformer(self.model_name)
                except Exception:
                    # Fallback to local deterministic hash/dense embedding
                    self._model = "fallback"

    def embed_texts(self, texts: List[str]) -> np.ndarray:
        self.load_model()
        if self._model != "fallback":
            try:
                embeddings = self._model.encode(texts, show_progress_bar=False, normalize_embeddings=True)
                return np.array(embeddings, dtype=np.float32)
            except Exception:
                pass
        return self._fallback_embeddings(texts)

    def embed_query(self, query: str) -> np.ndarray:
        return self.embed_texts([query])[0]

    def _fallback_embeddings(self, texts: List[str], dim: int = 384) -> np.ndarray:
        """Deterministic hashing fallback when model weights cannot be loaded without internet"""
        import hashlib
        embeddings = []
        for text in texts:
            words = text.lower().split()
            vec = np.zeros(dim, dtype=np.float32)
            for word in words:
                h = int(hashlib.md5(word.encode()).hexdigest(), 16)
                idx = h % dim
                sign = 1.0 if (h // dim) % 2 == 0 else -1.0
                vec[idx] += sign
            norm = np.linalg.norm(vec)
            if norm > 0:
                vec /= norm
            embeddings.append(vec)
        return np.array(embeddings, dtype=np.float32)
