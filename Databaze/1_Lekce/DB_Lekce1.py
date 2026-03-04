import sqlite3
from pathlib import Path

cesta = Path(__file__).with_name("database.db")
print("Cesta:", cesta)
print("Existuje databáze ve složce?", cesta.exists())



