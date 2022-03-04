from flask import Flask, render_template, request, url_for, redirect, abort, render_template
app = Flask(__name__)

import mysql.connector

mi_DB= mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="prueba"
)

cursor = mi_DB.cursor(dictionary=True)

@app.route('/')
def index():
    return 'Hola mundo'

# GET(mostrar) / POST(crear) / PUT(reemplazar) / PATCH(actualizar) / DELETE(eliminar)
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
    if request.method == 'GET':
        return 'El id del post es: ' + post_id
    else:
        return 'Este es otro metodo y no GET'

@app.route('/lele', methods=['POST', 'GET'])
def lele():
    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()
    print(usuarios)

    #abort(401)
    #return redirect(url_for('lala', post_id=2))
    return render_template('lele.html', usuarios=usuarios)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola Mundo')


#CREANDO UN REGISTRO DE USUARIO
@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        sql = "insert into usuario(username, email, edad) values(%s, %s, %s)"
        values = (username, email, edad)
        cursor.execute(sql, values)
        mi_DB.commit()

        return redirect(url_for('lele'))

    return render_template('crear.html')