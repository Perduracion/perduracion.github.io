from flask import Flask, request, url_for, redirect, flash
from flask import render_template
from flask_mysqldb import MySQL
import os.path

app = Flask(__name__,
            static_url_path = '', 
            static_folder ='static',
            template_folder ='templates'
)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '$Maria!'
app.config['MYSQL_DB'] = 'manjar'
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/acerca')
def acerca():
    return render_template('Acerca.html')

@app.route('/contacto')
def contacto():
    return render_template('Contacto.html')

@app.route('/sucursales')
def sucursales():
    return render_template('sucursales.html')

@app.route('/login')
def login():
    return render_template('/login.html')


@app.route('/register')
def register():
    return render_template('/register.html')


#@app.route('/')
#def index():
#    return render_template('index.html')
"""def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM USER')
    data = cur.fetchall()
    print (data)
    return render_template('index.html', users =data)
"""

"""
@app.route('/register', methods=['POST'])
def add_user():
    if request.method == 'POST':        
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cur= mysql.connection.cursor()
        cur.execute('INSERT INTO USER (USER_NAME, USER_MAIL, USER_PASSWORD) VALUES (%s, %s, %s)',
        (name,email, password))
        mysql.connection.commit()
        flash('contact add successfuly')
    
    return redirect('/')
"""

@app.route('/register', methods=['POST'])
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
        cur = mysql.connection.cursor()
        name_exists = cur.execute('SELECT * FROM USER WHERE USER_NAME = %s', [name]) 
        mail_exists = cur.execute('SELECT * FROM USER WHERE USER_MAIL = %s', [email])
        if name_exists:  # Corrección del chequeo de resultado de la consulta
            flash('El usuario ingresado ya existe en el sistema, por favor ingrese otro!')  # el usuario debe ser unico
        elif mail_exists:
            flash('El mail ya se encuentra registrado!')  # el mail debe ser unico
        else: 
            cur.execute('INSERT INTO USER (USER_NAME, USER_MAIL, USER_PASSWORD) VALUES (%s, %s, %s)',
                        (name, email, password))
            mysql.connection.commit()
            flash('Usuario registrado exitosamente')
            #return redirect('/register')  
    return render_template('/register.html')  


@app.route('/edit')
def edit():
    return 'edit'

@app.route('/delete')
def delete():
    return 'deelte'


#==================================================
#==================================================

# hay que crear los productos en la base de datos y traerlo para mostrar y elegir que comprar
# si hay tiempo hay que hacer un trigger que elimine el stock cuando alguien proceso la compra
# hay que crear el carrito de compras con un poco mas de estilo y fotos

productos = {
    '1': {'nombre': 'canelones', 'precio': 10},
    '2': {'nombre': 'fajitas', 'precio': 20},
    '3': {'nombre': 'pan arabe', 'precio': 30}
}

carrito = []

@app.route('/cart')
def cart():
    return render_template('cart.html', productos=productos, carrito=carrito)

@app.route('/agregar/<id>')
def agregar_producto(id):
    producto = productos.get(id)
    if producto:
        carrito.append(producto)
    return redirect(url_for('cart'))

@app.route('/limpiar')
def limpiar_carrito():
    carrito.clear()
    return redirect(url_for('cart'))













if __name__ == '__main__':
    app.run(port = 3000, debug = True) 
