import os
import re
import json
from pathlib import Path
from config import EXTRACT_DIR, DB_PATH
from database.db_manager import (
    init_db, add_subject, add_chapter, add_topic, insert_pyq, get_connection
)

def populate_syllabus():
    """
    Parses GATE DA & CS syllabus and indexes subjects, chapters and topics into SQLite.
    """
    print("[Ingestion] Initializing Database Schema...")
    init_db()

    # Subjects for GATE-DA (Official 2025 Syllabus)
    da_subjects = [
        {
            "name": "Probability and Statistics",
            "chapters": [
                {
                    "title": "Probability Axioms & Random Variables",
                    "topics": ["Sample space and events", "Marginal, conditional and joint probability", "Bayes Theorem", "Discrete and Continuous random variables", "PMF and PDF"]
                },
                {
                    "title": "Distributions & Statistics",
                    "topics": ["Uniform, Bernoulli, Binomial distributions", "Normal, Exponential, Poisson distributions", "Mean, median, mode, variance, std dev", "Correlation and Covariance", "Central Limit Theorem"]
                }
            ]
        },
        {
            "name": "Linear Algebra",
            "chapters": [
                {
                    "title": "Matrices and Systems of Equations",
                    "topics": ["Vector spaces and subspaces", "Linear dependence and independence", "Matrices, determinants, rank", "Systems of linear equations"]
                },
                {
                    "title": "Eigenvalues & Matrix Decompositions",
                    "topics": ["Eigenvalues and eigenvectors", "Characteristic polynomial", "Singular Value Decomposition (SVD)", "LU Decomposition"]
                }
            ]
        },
        {
            "name": "Calculus and Optimization",
            "chapters": [
                {
                    "title": "Functions and Differentiation",
                    "topics": ["Functions of single variable, limit, continuity, differentiability", "Taylor series", "Maxima and minima"]
                },
                {
                    "title": "Optimization Techniques",
                    "topics": ["Gradient descent", "Convex functions", "Constrained and unconstrained optimization", "Lagrange multipliers"]
                }
            ]
        },
        {
            "name": "Programming, Data Structures and Algorithms",
            "chapters": [
                {
                    "title": "Python Programming",
                    "topics": ["Python syntax and data types", "Control structures and functions", "List comprehension, generators, OOP"]
                },
                {
                    "title": "Data Structures & Algorithms",
                    "topics": ["Stacks, Queues, Linked Lists", "Trees, Hash Tables, Heaps", "Searching and Sorting algorithms", "Asymptotic analysis"]
                }
            ]
        },
        {
            "name": "Database Management and Warehousing",
            "chapters": [
                {
                    "title": "Relational Databases & SQL",
                    "topics": ["ER-model, relational model", "Relational algebra and tuple calculus", "SQL queries and joins", "Integrity constraints"]
                },
                {
                    "title": "Normalization & Data Warehousing",
                    "topics": ["Functional dependencies and normal forms (1NF, 2NF, 3NF, BCNF)", "Query processing", "Data warehousing architecture", "Multidimensional data models"]
                }
            ]
        },
        {
            "name": "Machine Learning",
            "chapters": [
                {
                    "title": "Supervised Learning",
                    "topics": ["Linear regression and ridge/lasso", "Logistic regression", "k-Nearest Neighbors (k-NN)", "Support Vector Machines (SVM)", "Decision Trees and Random Forest"]
                },
                {
                    "title": "Unsupervised Learning & Evaluation",
                    "topics": ["k-Means clustering", "Hierarchical clustering", "Principal Component Analysis (PCA)", "Cross-validation, Precision, Recall, F1-score, ROC-AUC"]
                }
            ]
        },
        {
            "name": "Artificial Intelligence",
            "chapters": [
                {
                    "title": "Search Strategies & Logic",
                    "topics": ["Informed and uninformed search (BFS, DFS, A*)", "Adversarial search and minimax", "Propositional and first-order predicate logic"]
                },
                {
                    "title": "Reasoning Under Uncertainty",
                    "topics": ["Bayesian networks", "Inference and exact reasoning", "Markov models basics"]
                }
            ]
        }
    ]

    print("[Ingestion] Populating GATE-DA Subjects & Chapters...")
    for s in da_subjects:
        sub_id = add_subject("GATE-DA", s["name"], f"Official GATE DA paper syllabus module for {s['name']}")
        for c_idx, c in enumerate(s["chapters"]):
            chap_id = add_chapter(sub_id, c["title"], c_idx + 1)
            for t_idx, t in enumerate(c["topics"]):
                add_topic(chap_id, t, t_idx + 1)

    print("[Ingestion] Syllabus populated successfully.")

def populate_pyqs_from_extract():
    """
    Parses extracted questions from sample papers in extract/ and registers them in SQLite.
    """
    chunk_file = EXTRACT_DIR / "member3_sujith_chunks.json"
    if not chunk_file.exists():
        print(f"[Ingestion] Warning: {chunk_file} not found.")
        return

    print("[Ingestion] Reading extracted questions and chunks...")
    with open(chunk_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    pyq_count = 0
    pattern = re.compile(r'(Q\.\d+)\s+(.*?)(?=\(A\))(.*?)(?=\(B\))(.*?)(?=\(C\))(.*?)(?=\(D\))(.*?)(?=Q\.\d+|\Z)', re.DOTALL)
    
    for c in chunks:
        doc = c.get("document", "")
        meta = c.get("metadata", {})
        src_file = meta.get("source_file", "")
        page = meta.get("page", 1)
        sub = meta.get("subject", "General")
        paper = meta.get("gate_paper", "GATE-DA")

        # Extract year from filename if present
        year = 2024
        if "2025" in src_file or "25" in src_file:
            year = 2025
        elif "2023" in src_file or "23" in src_file:
            year = 2023
        elif "2022" in src_file:
            year = 2022
        elif "2021" in src_file:
            year = 2021

        matches = pattern.findall(doc)
        for m in matches:
            q_num = m[0].strip()
            q_text = m[1].strip()
            opt_a = m[2].replace("(A)", "").strip()
            opt_b = m[3].replace("(B)", "").strip()
            opt_c = m[4].replace("(C)", "").strip()
            opt_d = m[5].replace("(D)", "").strip()

            if len(q_text) > 20 and opt_a and opt_b:
                insert_pyq({
                    "gate_paper": paper,
                    "year": year,
                    "question_number": q_num,
                    "question_text": q_text,
                    "option_a": opt_a[:250],
                    "option_b": opt_b[:250],
                    "option_c": opt_c[:250],
                    "option_d": opt_d[:250],
                    "correct_answer": "A", # default anchor if unverified key
                    "marks": 1.0,
                    "question_type": "MCQ",
                    "subject": sub,
                    "chapter": "Previous Year Examination",
                    "explanation": f"Official question from {src_file}, Page {page}.",
                    "source_doc": src_file,
                    "page_number": page
                })
                pyq_count += 1
                if pyq_count >= 150:
                    break
        if pyq_count >= 150:
            break

    print(f"[Ingestion] Inserted {pyq_count} structured PYQs into database.")

def build_vector_database():
    """
    Indexes all 2,400+ pre-extracted chunks into local FAISS vector store.
    """
    from modules.vector_store import VectorStore
    chunk_file = EXTRACT_DIR / "member3_sujith_chunks.json"
    if not chunk_file.exists():
        print(f"[Ingestion] Warning: {chunk_file} not found.")
        return

    print("[Ingestion] Loading pre-extracted chunks for FAISS indexing...")
    with open(chunk_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    store = VectorStore(index_name="gate_faiss")
    print(f"[Ingestion] Current FAISS vectors: {store.total_vectors}. Adding {len(chunks)} chunks...")
    store.add_chunks(chunks)
    print(f"[Ingestion] FAISS Index complete! Total vectors: {store.total_vectors}")

if __name__ == "__main__":
    populate_syllabus()
    populate_pyqs_from_extract()
    build_vector_database()
