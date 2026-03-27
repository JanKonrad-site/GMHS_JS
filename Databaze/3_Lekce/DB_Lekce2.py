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
def write_data():
    title = input("Název filmu: ").strip()
    year_text = input("Rok (ENTER = nevyplnit): ").strip()
    year = int(year_text) if year_text else None

    conn = sqlite3.connect(str(DB_FILE))

    conn.execute("INSERT INTO database (title, year) VALUES (?, ?);", (title, year))

    conn.commit()
    conn.close()
def read_data():
  

    conn = sqlite3.connect(str(DB_FILE))

    rows = conn.execute("SELECT id, title, year FROM database ORDER BY id DESC;").fetchall()

    conn.close()

    print("Počet záznamů:", len(rows))
    print("Obsah databáze:")
    for row in rows:
        print(row)

    input("ENTER...")

print("Uloženo.")
input("ENTER...")
create_table_movies()
print("Cesta:", DB_FILE)
print("Existuje databáze ve složce?", DB_FILE.exists())
print_table()
write_data()
read_data()


