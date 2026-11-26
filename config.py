import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
SYLLABUS_DIR = DATA_DIR / "syllabus"
STUDY_MATERIALS_DIR = DATA_DIR / "study_materials"
PYQ_DIR = DATA_DIR / "previous_year_questions"
ANSWER_KEYS_DIR = DATA_DIR / "answer_keys"
TEXTBOOKS_DIR = DATA_DIR / "textbooks"
PROCESSED_DIR = DATA_DIR / "processed"
EXTRACT_DIR = BASE_DIR / "extract"
SAMPLE_QUESTIONS_DIR = BASE_DIR / "sample questions"
SYLLABUS_PDF_DIR = BASE_DIR / "syllabuspdf"

VECTOR_DB_DIR = BASE_DIR / "vector_db"
GENERATED_LESSONS_DIR = BASE_DIR / "generated_lessons"
CHAT_HISTORY_DIR = BASE_DIR / "chat_history"
DATABASE_DIR = BASE_DIR / "database"
DB_PATH = DATABASE_DIR / "gate_tutor.db"

# LLM & Embedding Settings
# Preferred model
DEFAULT_LLM_MODEL = "mistral:3b"
FALLBACK_LLM_MODEL = "llama3.2:3b"
OLLAMA_BASE_URL = "http://localhost:11434"

# Embedding Model (Offline HuggingFace / SentenceTransformers)
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Chunking Settings
CHUNK_SIZE = 700
CHUNK_OVERLAP = 120

# UI Settings
APP_TITLE = "GATE AI TUTOR"
APP_SUBTITLE = "Syllabus-Based AI Tutor for GATE Exam Preparation Using Quantized LLMs"
