import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).with_name("movies.db")

def create_table_movies():
    conn = sqlite3.connect(DB_FILE)
    conn.execute(""" CREATE TABLE IF NOT EXISTS movies (
                 ID
                 title
                 year
                 ); """)
    conn.commit()
    conn.close()

create_table_movies()


   