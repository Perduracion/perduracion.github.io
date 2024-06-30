from flask import Flask, request, url_for, redirect, flash
from flask import render_template
from flask_mysqldb import MySQL
import os.path
from app.database import get_db
from app.view import *

app = Flask(__name__,
            static_url_path = '', 
            static_folder ='static',
            template_folder ='templates'
)

def index():
    return render_template('index.html')

def acerca():
    return render_template('Acerca.html')

def contacto():
    return render_template('Contacto.html')

def sucursales():
    return render_template('sucursales.html')

def login():
    return render_template('login.html')

def register():
    return render_template('register.html')

def nuevo():
    return render_template('nuevo.html')

def add_user():
    
    """ Definición de la función para agregar un usuario nuevo a la base de datos
        // validamos el usuario que debe ser único
        // validamos el correo electrónico si ya esta registrado en la base de datos
        // si cumple las condiciones se agregará el usuario nuevo    
    """
    if request.method == 'POST':  # Cambio "request.method == 'POST':" a "if request.method == 'POST':"
        name = request.form['name']
        email = request.form['email']  # Corrección de variable de usuario a email
        password = request.form['password']
        db = get_db()
        cur = db.cursor(buffered=True)
        
        cur.execute('SELECT * FROM USER WHERE USER_NAME = %s', [name])
        name_exists = cur.fetchone() is not None  # Check if any row is returned
        
        cur.execute('SELECT * FROM USER WHERE USER_MAIL = %s', [email])
        mail_exists = cur.fetchone() is not None  # Check if any row is returned
        if name_exists:  # Corrección del chequeo de resultado de la consulta
            flash('El usuario ya existe, intente con otro!')  # el usuario debe ser unico
        elif mail_exists:
            flash('El mail ya esta registrado!')  # el mail debe ser unico
        else: 
            cur.execute('INSERT INTO USER (USER_NAME, USER_MAIL, USER_PASSWORD) VALUES (%s, %s, %s)',
                        (name, email, password))
            db.commit()
            flash('Usuario registrado exitosamente')
            #return redirect('/register')  
    return render_template('/register.html')  




#if __name__ == '__main__':
    #app.run(port = 3000, debug = True) 
