from datetime import datetime
import sqlite3

def setup_db():
    conn = sqlite3.connect("sentiment_logs.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            polarity REAL,
            subjectivity REAL,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_to_db(text, polarity, subjectivity):
    conn = sqlite3.connect("sentiment_logs.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO logs (text, polarity, subjectivity, timestamp) VALUES (?, ?, ?, ?)",
        (text, polarity, subjectivity, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()