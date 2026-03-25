import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).with_name("database.db")

def create_table_movies():
    conn = sqlite3.connect(DB_FILE)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS database(
                 id     INTEGER PRIMARY KEY AUTOINCREMENT,
                 title  TEXT    NOT NULL,
                 year   INTEGER
                 ); """)
    conn.commit()
    conn.close()

def print_table():
    conn = sqlite3.connect(str(DB_FILE))
    rows = conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    conn.close()

    print("Tabulky v databázi:", rows)
    input("ENTER")

create_table_movies()
print("Cesta:", DB_FILE)
print("Existuje databáze ve složce?", DB_FILE.exists())
print_table()


