import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).resolve().with_name("reservations.db")


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


def add_reservation_record(name, date, arrival, departure):
    conn = connect()
    conn.execute(
        "INSERT INTO reservations (name, date, arrival, departure) VALUES (?, ?, ?, ?);",
        (name, date, arrival, departure)
    )
    conn.commit()
    conn.close()


def fetch_reservations():
    conn = connect()
    rows = conn.execute("""
        SELECT id, name, date, arrival, departure
        FROM reservations
        ORDER BY date ASC, arrival ASC;
    """).fetchall()
    conn.close()
    return rows


def refresh_table():
    for item in tree.get_children():
        tree.delete(item)

    rows = fetch_reservations()
    for row in rows:
        tree.insert("", tk.END, values=row)


def save_reservation():
    name = entry_name.get().strip()
    date = entry_date.get().strip()
    arrival = entry_arrival.get().strip()
    departure = entry_departure.get().strip()

    if not name or not date or not arrival or not departure:
        messagebox.showwarning("Chyba", "Vyplň všechna pole.")
        return

    add_reservation_record(name, date, arrival, departure)
    messagebox.showinfo("Hotovo", "Rezervace byla uložena.")

    entry_name.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_arrival.delete(0, tk.END)
    entry_departure.delete(0, tk.END)

    refresh_table()


init_db()

root = tk.Tk()
root.title("Rezervační systém")
root.geometry("760x500")

frame_form = tk.Frame(root, padx=10, pady=10)
frame_form.pack(fill="x")

tk.Label(frame_form, text="Jméno:").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_form, width=25)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Datum (YYYY-MM-DD):").grid(row=1, column=0, sticky="w")
entry_date = tk.Entry(frame_form, width=25)
entry_date.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Příchod (HH:MM):").grid(row=2, column=0, sticky="w")
entry_arrival = tk.Entry(frame_form, width=25)
entry_arrival.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Odchod (HH:MM):").grid(row=3, column=0, sticky="w")
entry_departure = tk.Entry(frame_form, width=25)
entry_departure.grid(row=3, column=1, padx=5, pady=5)

btn_save = tk.Button(frame_form, text="Přidat rezervaci", command=save_reservation)
btn_save.grid(row=4, column=0, columnspan=2, pady=10)

frame_table = tk.Frame(root, padx=10, pady=10)
frame_table.pack(fill="both", expand=True)

columns = ("id", "name", "date", "arrival", "departure")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")

tree.heading("id", text="ID")
tree.heading("name", text="Jméno")
tree.heading("date", text="Datum")
tree.heading("arrival", text="Příchod")
tree.heading("departure", text="Odchod")

tree.column("id", width=50)
tree.column("name", width=180)
tree.column("date", width=120)
tree.column("arrival", width=100)
tree.column("departure", width=100)

tree.pack(fill="both", expand=True)

refresh_table()

root.mainloop()