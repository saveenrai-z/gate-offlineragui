import fitz  # PyMuPDF
from pathlib import Path
from typing import List, Dict, Any

class PDFProcessor:
    @staticmethod
    def extract_text_from_pdf(filepath: str) -> List[Dict[str, Any]]:
        """
        Extracts text from PDF page by page with metadata.
        Returns a list of dicts: [{'page_number': int, 'text': str, 'char_count': int, 'file_name': str}]
        """
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")

        results = []
        doc = fitz.open(str(path))
        for page_idx in range(len(doc)):
            page = doc[page_idx]
            text = page.get_text("text")
            cleaned_text = PDFProcessor.clean_text(text)
            results.append({
                "file_name": path.name,
                "relative_path": str(path),
                "page_number": page_idx + 1,
                "text": cleaned_text,
                "char_count": len(cleaned_text),
                "extractor": "pymupdf"
            })
        doc.close()
        return results

    @staticmethod
    def clean_text(text: str) -> str:
        """Cleans irregular whitespace, repeated linebreaks, etc."""
        if not text:
            return ""
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return "\n".join(lines)
