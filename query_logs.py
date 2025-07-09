import sqlite3


def show_logs():
    conn = sqlite3.connect("sentiment_logs.db")
    c = conn.cursor()
    c.execute("SELECT * FROM logs")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == "__main__":
    show_logs()