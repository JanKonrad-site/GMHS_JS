import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).resolve().with_name("reservations.db")

# =========================================================
# FUNKCE (sem vkládáš bloky)
# =========================================================
def connect():
    return sqlite3.connect(str(DB_FILE))

def init_db():
    conn = connect()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        name      TEXT    NOT NULL,
        date      TEXT    NOT NULL,
        arrival   TEXT    NOT NULL,
        departure TEXT    NOT NULL
    );
    """)
    conn.commit()
    conn.close()

def add_reservation():
    name = input("Jméno: ").strip()
    date = input("Datum (YYYY-MM-DD): ").strip()
    arrival = input("Příchod (HH:MM): ").strip()
    departure = input("Odchod (HH:MM): ").strip()

    conn = connect()
    conn.execute(
        "INSERT INTO reservations (name, date, arrival, departure) VALUES (?, ?, ?, ?);",
        (name, date, arrival, departure)
    )
    conn.commit()
    conn.close()
    print("Uloženo.")

def fetch_reservations():
    conn = connect()
    rows = conn.execute("""
        SELECT id, name, date, arrival, departure
        FROM reservations
        ORDER BY date ASC, arrival ASC;
    """).fetchall()
    conn.close()
    return rows

def print_reservations(rows):
    if not rows:
        print("Žádné rezervace.")
        return

    print("Rezervace:")
    for (rid, name, date, arrival, departure) in rows:
        print(f"#{rid} | {name} | {date} | {arrival}-{departure}")

def menu():
    print()
    print("1) Přidat rezervaci")
    print("2) Vypsat rezervace")
    print("0) Konec")

# =========================================================
# MAIN
# =========================================================
if __name__ == "__main__":
    init_db()

    while True:
        menu()
        choice = input("Volba: ").strip()

        if choice == "1":
            add_reservation()

        elif choice == "2":
            rows = fetch_reservations()
            print_reservations(rows)

        elif choice == "0":
            break

        else:
            print("Neplatná volba.")