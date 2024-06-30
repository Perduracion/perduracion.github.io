from flask import jsonify, request
# from app.model import Movie
from app.model import Product
def index():
    return jsonify({'status': 'API - Online'})


def get_all_products():
    products = Product.get_all()
    return jsonify([product.serialize() for product in products])


def create_product():
    data = request.json
    n_product = Product(product_name=data['product_name'], 
                        product_desc=data['product_desc'], 
                        product_image_path=data['product_image_path'], 
                        product_price=data['product_price'],
                        product_cat_id=data['product_cat_id'],)
    n_product.save()
    return jsonify({'message': 'Product added successfully'}), 201


def get_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify(product.serialize())



# def get_all_movies():
#     movies = Product.get_all()
#     return jsonify([movie.serialize() for movie in movies])


def update_movie(movie_id):
    movie = Movie.get_by_id(movie_id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    data = request.json
    movie.title = data['title']
    movie.director = data['director']
    movie.release_date = data['release_date']
    movie.banner = data['banner']
    movie.save()
    return jsonify({'message': 'Movie updated successfully'})

def delete_movie(movie_id):
    movie = Movie.get_by_id(movie_id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    movie.delete()
    return jsonify({'message': 'Movie deleted successfully'})