import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Rezervační systém")
root.geometry("760x500")


# =========================================================
# HLAVIČKA
# =========================================================
label_title = tk.Label(root, text="Rezervační systém", font=("Arial", 22, "bold"))
label_title.pack(pady=(15, 5))

label_subtitle = tk.Label(root, text="Správa rezervací", font=("Arial", 12))
label_subtitle.pack(pady=(0, 15))


# =========================================================
# FORMULÁŘ
# =========================================================
frame_form = tk.LabelFrame(root, text="Nová rezervace", padx=10, pady=10)
frame_form.pack(fill="x", padx=15, pady=10)

tk.Label(frame_form, text="Jméno:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_name = tk.Entry(frame_form, width=35)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Datum (YYYY-MM-DD):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_date = tk.Entry(frame_form, width=35)
entry_date.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Příchod (HH:MM):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_arrival = tk.Entry(frame_form, width=35)
entry_arrival.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Odchod (HH:MM):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
entry_departure = tk.Entry(frame_form, width=35)
entry_departure.grid(row=3, column=1, padx=5, pady=5)

btn_add = tk.Button(frame_form, text="Přidat rezervaci")
btn_add.grid(row=4, column=0, padx=5, pady=10)

btn_clear = tk.Button(frame_form, text="Vyčistit")
btn_clear.grid(row=4, column=1, padx=5, pady=10, sticky="w")


# =========================================================
# TABULKA
# =========================================================
frame_table = tk.LabelFrame(root, text="Seznam rezervací", padx=10, pady=10)
frame_table.pack(fill="both", expand=True, padx=15, pady=10)

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


# =========================================================
# UKÁZKOVÁ DATA DO TABULKY
# =========================================================
sample_rows = [
    (1, "Jan Novák", "2024-06-15", "14:00", "16:00"),
    (2, "Anna Malá", "2024-06-16", "09:30", "11:00"),
    (3, "Petr Dvořák", "2024-06-17", "10:00", "12:30"),
]

for row in sample_rows:
    tree.insert("", tk.END, values=row)


root.mainloop()