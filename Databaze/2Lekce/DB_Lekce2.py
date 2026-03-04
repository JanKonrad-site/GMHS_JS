import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).resolve().with_name("movies.db")
def open_and_close_db():
    print("DB path:", DB_FILE)
    print("DB exists before connect:", DB_FILE.exists())

    conn = sqlite3.connect(str(DB_FILE))
    conn.close()

    print("DB exists after close:", DB_FILE.exists())
def create_table_movies():
    conn = sqlite3.connect(str(DB_FILE))

    conn.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT    NOT NULL,
        year  INTEGER
    );
    """)

    conn.commit()
    conn.close()
if __name__ == "__main__":
    open_and_close_db()
    create_table_movies()
    input("ENTER pro ukončení...")

