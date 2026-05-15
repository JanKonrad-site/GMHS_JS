import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Rezervační systém")
root.geometry("760x500")

title_label = tkinter.Label(root, text="Rezervační systém", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

subtitle_label = tkinter.Label(root, text="Grafická příprava aplikace")
subtitle_label.pack(pady=5)

form_frame = tkinter.LabelFrame(root, text="Nová rezervace", padx=10, pady=10)
form_frame.pack(fill="x", padx=15, pady=10)

label_name = tkinter.Label(form_frame, text="Jméno:")
label_name.pack()

entry_name = tkinter.Entry(form_frame, width=40)
entry_name.pack(pady=5)

label_date = tkinter.Label(form_frame, text="Datum (YYYY-MM-DD):")
label_date.pack()

entry_date = tkinter.Entry(form_frame, width=40)
entry_date.pack(pady=5)

label_arrival = tkinter.Label(form_frame, text="Příchod (HH:MM):")
label_arrival.pack()

entry_arrival = tkinter.Entry(form_frame, width=40)
entry_arrival.pack(pady=5)

label_departure = tkinter.Label(form_frame, text="Odchod (HH:MM):")
label_departure.pack()

entry_departure = tkinter.Entry(form_frame, width=40)
entry_departure.pack(pady=5)

button_add = tkinter.Button(form_frame, text="Přidat rezervaci")
button_add.pack(pady=10)

table_frame = tkinter.LabelFrame(root, text="Seznam rezervací", padx=10, pady=10)
table_frame.pack(fill="both", expand=True, padx=15, pady=10)

tree = ttk.Treeview(
    table_frame,
    columns=("id", "name", "date", "arrival", "departure"),
    show="headings"
)

tree.heading("id", text="ID")
tree.heading("name", text="Jméno")
tree.heading("date", text="Datum")
tree.heading("arrival", text="Příchod")
tree.heading("departure", text="Odchod")

tree.pack(fill="both", expand=True)

root.mainloop()