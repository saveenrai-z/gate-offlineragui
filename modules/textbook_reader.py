import os
import pymupdf
from typing import List, Dict, Any

class TextbookReader:
    # Calibrated exact starting and ending pages for each GATE-DA subject
    MAPPING = {
        "Probability and Statistics": [
            ("mml-book.pdf", 178, 225),  # Chapter 6: Probability and Distributions, sample space, Bayes theorem, distributions
        ],
        "Linear Algebra": [
            ("mml-book.pdf", 20, 95),    # Chapter 2: Linear Algebra, Systems of equations, Vector spaces, matrices
        ],
        "Calculus and Optimization": [
            ("mml-book.pdf", 135, 165),  # Chapter 5: Vector Calculus
            ("mml-book.pdf", 225, 260),  # Chapter 7: Continuous Optimization
        ],
        "Programming, Data Structures and Algorithms": [
            ("english_18_python_programming.pdf", 15, 300),
            ("english_19_discrete_structures.pdf", 15, 300),
        ],
        "Database Management and Warehousing": [
            ("english_19_discrete_structures.pdf", 250, 450),
        ],
        "Machine Learning": [
            ("mml-book.pdf", 280, 410),  # Chapters 9-12: Linear Regression, PCA, GMM, SVM
        ],
        "Artificial Intelligence": [
            ("textbook_full.pdf", 1, 185), # Full Introduction to AI Textbook
        ]
    }

    @classmethod
    def get_detailed_teachings(cls, subject_name: str, topic_title: str) -> Dict[str, Any]:
        """
        Directly reads textbook pages for the target topic, filtering out headers and
        formatting into clean academic markdown.
        """
        matched_configs = cls.MAPPING.get(subject_name, [("mml-book.pdf", 20, 100)])
        extracted_pages = []
        sources = []

        # Extract words from topic for scoring
        keywords = [k.lower() for k in topic_title.replace(",", " ").replace("&", " ").split() if len(k) > 2]

        for filename, start_p, end_p in matched_configs:
            filepath = os.path.join("syllabuspdf", filename)
            if not os.path.exists(filepath):
                continue

            try:
                doc = pymupdf.open(filepath)
                max_page = min(len(doc), end_p)
                for p in range(start_p - 1, max_page):
                    text = doc[p].get_text("text")
                    if not text or len(text.strip()) < 80:
                        continue
                    
                    lower = text.lower()
                    # Check how many topic keywords match this page
                    matched_kws = [kw for kw in keywords if kw in lower]
                    if len(matched_kws) >= 1 or len(keywords) == 0:
                        # Clean lines
                        lines = [line.strip() for line in text.splitlines() if line.strip()]
                        # Remove page header numbers like '175 Probability and Distributions'
                        clean_lines = []
                        for l in lines:
                            if len(l) < 5 and l.isdigit():
                                continue
                            clean_lines.append(l)

                        page_prose = " ".join(clean_lines)
                        page_prose = page_prose.replace("Definition", "\n\n**Definition:**")
                        page_prose = page_prose.replace("Example", "\n\n**Example:**")
                        page_prose = page_prose.replace("Remark", "\n\n**Remark:**")
                        
                        extracted_pages.append(page_prose)
                        sources.append({
                            "source_file": filename,
                            "page": p + 1
                        })
                        if len(extracted_pages) >= 3:
                            break
                doc.close()
            except Exception as e:
                print(f"[TextbookReader] Error: {e}")

            if len(extracted_pages) >= 3:
                break

        if not extracted_pages:
            content = f"### {topic_title}\n\nPlease review standard syllabus formulations for {subject_name} in {matched_configs[0][0]}."
        else:
            content = "\n\n---\n\n".join(extracted_pages[:3])

        return {
            "topic": topic_title,
            "subject": subject_name,
            "content": content,
            "sources": sources
        }
