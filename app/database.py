import os
import mysql.connector
from flask import g
from dotenv import load_dotenv


# Cargar variables de entorno desde el archivo .env
load_dotenv()

DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', 3306),
}


def get_db():
    print(DATABASE_CONFIG)
    if 'db' not in g:
        print(dir(g))
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)