from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app=Flask(__name__)

def conectar_base():
    conector=sqlite3.connect('tareas.db')
    conector.row_factory=sqlite3.Row
    return conector

@app.route("/")
def index():
   conector=conectar_base()
   tareas=conector.execute('SELECT * FROM tareas ORDER BY id').fetchall()
   return render_template('index.html',tareas=tareas)

@app.route("/agregar",methods=['POST'])
def agregar():
    if request.method=='POST':
        descripcion_nueva=request.form['descripcion']
        if descripcion_nueva:
            conector=conectar_base()
            conector.execute('INSERT INTO tareas (descripcion) VALUES (?)',(descripcion_nueva,))
            conector.commit()
            conector.close()
        return redirect(url_for('index'))
    
@app.route('/borrar/<int:tarea_id>',methods=['POST'])
def borrar_tarea (tarea_id):
    if request.method == 'POST':
        conector=conectar_base()
        conector.execute('DELETE FROM tareas WHERE id=?',(tarea_id,))
        conector.commit()
        conector.close()
    return redirect(url_for('index'))

@app.route('/completar/<int:tarea_id>', methods=['POST'])
def completar_tarea (tarea_id):
    if request.method=='POST':
        conector=conectar_base()
        conector.execute('UPDATE tareas SET completada = 1 WHERE id = ?', (tarea_id,))
        conector.commit()
        conector.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)