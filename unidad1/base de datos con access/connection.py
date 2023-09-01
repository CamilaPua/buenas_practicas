import sys
import pyodbc

def run():
    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\cuc\buenas_practicas\db_prueba.accdb;")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personas")

    for row in cursor.fetchall():
        print('-'*30 + f'\nID: {row[0]}\nNombre:{row[1]}\nEdad:{row[2]}\n' + '-'*30)


    print('\nPersonas menores o con 18 años')

    cursor.execute("SELECT * FROM personas WHERE edad <= 18")
    for row in cursor.fetchall():
        print('-'*30 + f'\nID: {row[0]}\nNombre:{row[1]}\nEdad:{row[2]}\n' + '-'*30)


    cursor.close
    conn.close


if __name__ == '__main__':
    run()
