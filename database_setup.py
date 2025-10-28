import sqlite3

conector=sqlite3.connect('tareas.db')
cursor=conector.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS tareas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   descripcion TEXT NOT NULL,
                   completada BOOLEAN NOT NULL DEFAULT 0 
               );
               """)

conector.commit()
conector.close()

print("Base de datos creada junto con la tabla tareas dentro")