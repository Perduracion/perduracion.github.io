from flask import Flask, flash, jsonify
from flask_cors import CORS
from app.database import init_app
from app.view import *
from flask_swagger import swagger
from src.routes.routes import *

app = Flask(__name__)

app.secret_key = 'mysecretkey'

# Configurar la aplicación Flask
# app.config.from_pyfile('config/development.py')

# Inicializar la base de datos con la aplicación Flask
init_app(app)
#permitir solicitudes desde cualquier origen
CORS(app)
#permitir solicitudes desde un origen específico
#CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}}) --- change port 3000

app.route('/')(index)
app.route('/acerca')(acerca)
app.route('/contacto')(contacto)
app.route('/sucursales')(sucursales)
app.route('/login')(login)
app.route('/register')(register)
app.route('/register', methods=['POST'])(add_user)

@app.route('/cart')
def show_products():
    products = Product.get_all()
    return render_template('cart.html', products=products)


app.route('/nuevo')(nuevo)



# # Rutas para el CRUD de la entidad Movie
app.route('/api', methods=['GET'])(api)
app.route('/api/productos/<int:product_id>', methods=['GET'])(get_product)
app.route('/api/products/', methods=['GET'])(get_all_products)
app.route('/api/products/', methods=['POST'])(create_product)
#app.route('/api/movies/<int:movie_id>', methods=['PUT'])(update_movie)
# app.route('/api/movies/<int:movie_id>', methods=['DELETE'])(delete_movie)

if __name__ == '__main__':
    app.run(port = 3000, debug=True)