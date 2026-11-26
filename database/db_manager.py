import sqlite3
from typing import List, Dict, Any, Optional
from config import DB_PATH, DATABASE_DIR

def get_connection() -> sqlite3.Connection:
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    schema_file = DATABASE_DIR / "schema.sql"
    with open(schema_file, "r", encoding="utf-8") as f:
        schema = f.read()
    with get_connection() as conn:
        conn.executescript(schema)

# Subject & Chapter Management
def add_subject(gate_paper: str, name: str, description: str = "") -> int:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO subjects (gate_paper, name, description) VALUES (?, ?, ?)",
            (gate_paper, name, description)
        )
        cursor.execute("SELECT id FROM subjects WHERE gate_paper = ? AND name = ?", (gate_paper, name))
        return cursor.fetchone()["id"]

def add_chapter(subject_id: int, title: str, chapter_order: int = 1) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO chapters (subject_id, title, chapter_order) VALUES (?, ?, ?)",
            (subject_id, title, chapter_order)
        )
        cursor.execute("SELECT id FROM chapters WHERE subject_id = ? AND title = ?", (subject_id, title))
        return cursor.fetchone()["id"]

def add_topic(chapter_id: int, title: str, topic_order: int = 1) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO topics (chapter_id, title, topic_order) VALUES (?, ?, ?)",
            (chapter_id, title, topic_order)
        )
        cursor.execute("SELECT id FROM topics WHERE chapter_id = ? AND title = ?", (chapter_id, title))
        return cursor.fetchone()["id"]

def get_all_subjects(gate_paper: Optional[str] = None) -> List[Dict[str, Any]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        if gate_paper:
            cursor.execute("SELECT * FROM subjects WHERE gate_paper = ? ORDER BY id", (gate_paper,))
        else:
            cursor.execute("SELECT * FROM subjects ORDER BY id")
        return [dict(row) for row in cursor.fetchall()]

def get_chapters_by_subject(subject_id: int) -> List[Dict[str, Any]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM chapters WHERE subject_id = ? ORDER BY chapter_order, id", (subject_id,))
        return [dict(row) for row in cursor.fetchall()]

def get_topics_by_chapter(chapter_id: int) -> List[Dict[str, Any]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT t.*, coalesce(p.completed, 0) as completed, coalesce(p.bookmarked, 0) as bookmarked
            FROM topics t
            LEFT JOIN student_progress p ON t.id = p.topic_id
            WHERE t.chapter_id = ?
            ORDER BY t.topic_order, t.id
        """, (chapter_id,))
        return [dict(row) for row in cursor.fetchall()]

def update_topic_progress(topic_id: int, completed: Optional[int] = None, bookmarked: Optional[int] = None):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student_progress WHERE topic_id = ?", (topic_id,))
        row = cursor.fetchone()
        if row:
            if completed is not None:
                cursor.execute("UPDATE student_progress SET completed = ?, updated_at = CURRENT_TIMESTAMP WHERE topic_id = ?", (completed, topic_id))
            if bookmarked is not None:
                cursor.execute("UPDATE student_progress SET bookmarked = ?, updated_at = CURRENT_TIMESTAMP WHERE topic_id = ?", (bookmarked, topic_id))
        else:
            comp = completed if completed is not None else 0
            bkm = bookmarked if bookmarked is not None else 0
            cursor.execute("INSERT INTO student_progress (topic_id, completed, bookmarked) VALUES (?, ?, ?)", (topic_id, comp, bkm))

# Lesson Cache
def save_lesson(chapter_id: int, lesson_json: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO lessons (chapter_id, lesson_json, created_at) VALUES (?, ?, CURRENT_TIMESTAMP)",
            (chapter_id, lesson_json)
        )

def get_lesson(chapter_id: int) -> Optional[str]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT lesson_json FROM lessons WHERE chapter_id = ?", (chapter_id,))
        row = cursor.fetchone()
        return row["lesson_json"] if row else None

# Previous Year Questions
def insert_pyq(data: Dict[str, Any]) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO previous_year_questions 
            (gate_paper, year, question_number, question_text, option_a, option_b, option_c, option_d, 
             correct_answer, marks, question_type, subject, chapter, explanation, source_doc, page_number)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data.get("gate_paper", "GATE-DA"),
            data.get("year", 2024),
            data.get("question_number", ""),
            data.get("question_text", ""),
            data.get("option_a", ""),
            data.get("option_b", ""),
            data.get("option_c", ""),
            data.get("option_d", ""),
            data.get("correct_answer", ""),
            data.get("marks", 1.0),
            data.get("question_type", "MCQ"),
            data.get("subject", ""),
            data.get("chapter", ""),
            data.get("explanation", ""),
            data.get("source_doc", ""),
            data.get("page_number", 1)
        ))
        return cursor.lastrowid

def get_pyqs(gate_paper: Optional[str] = None, year: Optional[int] = None, subject: Optional[str] = None) -> List[Dict[str, Any]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM previous_year_questions WHERE 1=1"
        params = []
        if gate_paper:
            query += " AND gate_paper = ?"
            params.append(gate_paper)
        if year:
            query += " AND year = ?"
            params.append(year)
        if subject:
            query += " AND subject LIKE ?"
            params.append(f"%{subject}%")
        query += " ORDER BY year DESC, id ASC"
        cursor.execute(query, tuple(params))
        return [dict(row) for row in cursor.fetchall()]

def record_pyq_attempt(pyq_id: int, selected_answer: str, is_correct: bool):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO student_pyq_attempts (pyq_id, selected_answer, is_correct) VALUES (?, ?, ?)",
            (pyq_id, selected_answer, 1 if is_correct else 0)
        )

# Chat History
def save_chat_message(scope: str, role: str, message: str, subject_id: Optional[int] = None, chapter_id: Optional[int] = None, sources: str = ""):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO doubts_chat (scope, subject_id, chapter_id, role, message, sources)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (scope, subject_id, chapter_id, role, message, sources))

def get_chat_history(scope: str, subject_id: Optional[int] = None, chapter_id: Optional[int] = None) -> List[Dict[str, Any]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        if scope == "chapter":
            cursor.execute("""
                SELECT * FROM doubts_chat 
                WHERE scope = 'chapter' AND chapter_id = ?
                ORDER BY created_at ASC
            """, (chapter_id,))
        else:
            cursor.execute("""
                SELECT * FROM doubts_chat 
                WHERE scope = 'general'
                ORDER BY created_at ASC
            """)
        return [dict(row) for row in cursor.fetchall()]

# Practice Test Result Recording
def record_practice_test(subject: str, chapter: str, total_questions: int, score: float, accuracy: float, test_data: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO practice_tests (subject, chapter, total_questions, score, accuracy, test_data)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (subject, chapter, total_questions, score, accuracy, test_data))

def get_stats() -> Dict[str, Any]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) as c FROM subjects")
        total_subjects = cursor.fetchone()["c"]
        cursor.execute("SELECT COUNT(*) as c FROM chapters")
        total_chapters = cursor.fetchone()["c"]
        cursor.execute("SELECT COUNT(*) as c FROM topics")
        total_topics = cursor.fetchone()["c"]
        cursor.execute("SELECT COUNT(*) as c FROM student_progress WHERE completed = 1")
        completed_topics = cursor.fetchone()["c"]
        cursor.execute("SELECT COUNT(*) as c FROM previous_year_questions")
        total_pyqs = cursor.fetchone()["c"]
        cursor.execute("SELECT COUNT(*) as c FROM student_pyq_attempts")
        attempts = cursor.fetchone()["c"]
        cursor.execute("SELECT COUNT(*) as c FROM student_pyq_attempts WHERE is_correct = 1")
        correct_attempts = cursor.fetchone()["c"]
        accuracy = round((correct_attempts / attempts * 100), 1) if attempts > 0 else 0.0

        return {
            "total_subjects": total_subjects,
            "total_chapters": total_chapters,
            "total_topics": total_topics,
            "completed_topics": completed_topics,
            "pending_topics": total_topics - completed_topics,
            "total_pyqs": total_pyqs,
            "pyq_attempts": attempts,
            "pyq_accuracy": accuracy
        }
