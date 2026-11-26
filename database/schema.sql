-- SQLite Schema for GATE AI Tutor

CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT UNIQUE NOT NULL,
    filepath TEXT NOT NULL,
    doc_type TEXT NOT NULL, -- syllabus, pyq, study_material, textbook, answer_key
    gate_paper TEXT,        -- GATE-DA, GATE-CS, etc.
    subject TEXT,
    page_count INTEGER,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gate_paper TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    UNIQUE(gate_paper, name)
);

CREATE TABLE IF NOT EXISTS chapters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    chapter_order INTEGER DEFAULT 1,
    FOREIGN KEY(subject_id) REFERENCES subjects(id) ON DELETE CASCADE,
    UNIQUE(subject_id, title)
);

CREATE TABLE IF NOT EXISTS topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    topic_order INTEGER DEFAULT 1,
    FOREIGN KEY(chapter_id) REFERENCES chapters(id) ON DELETE CASCADE,
    UNIQUE(chapter_id, title)
);

CREATE TABLE IF NOT EXISTS lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter_id INTEGER UNIQUE NOT NULL,
    lesson_json TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(chapter_id) REFERENCES chapters(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS student_progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER UNIQUE NOT NULL,
    completed INTEGER DEFAULT 0,
    bookmarked INTEGER DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(topic_id) REFERENCES topics(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS previous_year_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gate_paper TEXT NOT NULL,
    year INTEGER NOT NULL,
    question_number TEXT,
    question_text TEXT NOT NULL,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    correct_answer TEXT,
    marks REAL DEFAULT 1.0,
    question_type TEXT DEFAULT 'MCQ', -- MCQ, NAT, MSQ
    subject TEXT,
    chapter TEXT,
    explanation TEXT,
    source_doc TEXT,
    page_number INTEGER
);

CREATE TABLE IF NOT EXISTS student_pyq_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pyq_id INTEGER NOT NULL,
    selected_answer TEXT,
    is_correct INTEGER,
    attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(pyq_id) REFERENCES previous_year_questions(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS practice_tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    chapter TEXT,
    total_questions INTEGER,
    score REAL,
    accuracy REAL,
    test_data TEXT, -- JSON format of questions and student answers
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS doubts_chat (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scope TEXT NOT NULL, -- 'general' or 'chapter'
    subject_id INTEGER,
    chapter_id INTEGER,
    role TEXT NOT NULL,  -- 'user' or 'assistant'
    message TEXT NOT NULL,
    sources TEXT,        -- JSON array of source citations
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
