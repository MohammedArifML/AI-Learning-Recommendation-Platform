import sqlite3
import pandas as pd

DB_PATH = "storage/assessment_history.db"


def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


# ----------------------------------------------------
# CREATE TABLE
# ----------------------------------------------------


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS assessment_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            learner_name TEXT,
            learner_email TEXT,
            career_track TEXT,
            assessment_topic TEXT,
            score INTEGER,
            total_questions INTEGER,
            percentage REAL,
            difficulty TEXT,
            category TEXT,
            assessment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    conn.close()


# ----------------------------------------------------
# INSERT RESULT
# ----------------------------------------------------


def save_assessment_result(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO assessment_results (
            learner_name,
            learner_email,
            career_track,
            assessment_topic,
            score,
            total_questions,
            percentage,
            difficulty,
            category
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            data["learner_name"],
            data["learner_email"],
            data["career_track"],
            data["assessment_topic"],
            data["score"],
            data["total_questions"],
            data["percentage"],
            data["difficulty"],
            data["category"]
        )
    )

    conn.commit()
    conn.close()


# ----------------------------------------------------
# FETCH HISTORY
# ----------------------------------------------------


def get_assessment_history():
    conn = get_connection()

    query = "SELECT * FROM assessment_results ORDER BY assessment_date DESC"

    df = pd.read_sql(query, conn)

    conn.close()

    return df