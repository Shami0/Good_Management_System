import sqlite3
from pathlib import Path

DB_PATH = Path("productivity.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row 
    return conn

def initialize_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.executescript("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            total_lessons INTEGER DEFAULT 0,
            completed_lessons INTEGER DEFAULT 0,
            created_at TEXT DEFAULT (date('now'))
        );

        CREATE TABLE IF NOT EXISTS tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            color TEXT DEFAULT '#4A90D9'
        );

        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'pending',
            type TEXT DEFAULT 'daily',
            due_date TEXT,
            time_spent INTEGER DEFAULT 0,
            course_id INTEGER REFERENCES courses(id),
            created_at TEXT DEFAULT (date('now'))
        );

        CREATE TABLE IF NOT EXISTS task_tags (
            task_id INTEGER REFERENCES tasks(id),
            tag_id INTEGER REFERENCES tags(id),
            PRIMARY KEY (task_id, tag_id)
        );

        CREATE TABLE IF NOT EXISTS time_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER REFERENCES tasks(id),
            start_time TEXT,
            end_time TEXT,
            duration INTEGER
        );
    """)

    conn.commit()
    conn.close()