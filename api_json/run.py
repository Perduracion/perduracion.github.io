from flask import Flask
from flask_cors import CORS
from app.database import init_app
from app.view import *

def create_app():
    app = Flask(__name__)

    # Inicialización de la base de datos
    init_app(app)

    # Configuración de CORS
    CORS(app)

    # Rutas
    app.route('/', methods=['GET'])(index)
    app.route('/api/products/<int:product_id>', methods=['GET'])(get_product)
    app.route('/api/products/', methods=['GET'])(get_all_products)
    app.route('/api/products/', methods=['POST'])(create_product)
    app.route('/api/products/<int:product_id>', methods=['PUT'])(update_product)
    app.route('/api/products/<int:product_id>', methods=['DELETE'])(delete_product)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
