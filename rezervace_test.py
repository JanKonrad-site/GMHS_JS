import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Rezervační systém")
root.geometry("760x500")

frame = tkinter.LabelFrame(root, text="Nová rezervace", padx=10, pady=10)
frame.pack(padx=15, pady=15, fill="x")

label = tkinter.Label(frame, text="Jméno")
label.pack()

entry = tkinter.Entry(frame)
entry.pack()

button = tkinter.Button(frame, text="Přidat rezervaci")
button.pack()

three = ttk.Treeview(root, columns=("id", "name", "class"), show="headings")
three.heading("id", text="ID")
three.heading("name", text="Jméno")
three.heading("class", text="Třída")
three.pack(fill="both", expand=True)


root.mainloop()