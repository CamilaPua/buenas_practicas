import sys
import pyodbc

conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\cuc\buenas_practicas\db_prueba.accdb;")
cursor = conn.cursor()
cursor.execute("SELECT * FROM personas")

for row in cursor.fetchall():
    print(row)

cursor.close
conn.close
