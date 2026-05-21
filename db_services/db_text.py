import sqlite3

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DB_PATH = str(PROJECT_ROOT / "data" / "db_text.db")

def create():
    conn = sqlite3.connect(DB_PATH)

    with conn:
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS file_info (
                id INTEGER PRIMARY KEY,
                title TEXT,
                content TEXT
            )''')
    conn.close()

def save_info(title, content):
    conn = sqlite3.connect(DB_PATH)

    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO file_info (title, content) VALUES (?, ?)",
            (title, content)
        )
    conn.close()