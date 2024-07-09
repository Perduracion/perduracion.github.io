from flask import jsonify, request
from app.model import Product

def index():
    return jsonify({'status': 'API - Online'})

def get_all_products():
    products = Product.get_all()
    return jsonify([product.serialize() for product in products])

def create_product():
    data = request.get_json()
    new_product = Product(product_name=data['product_name'], 
                          product_desc=data['product_desc'], 
                          product_image_path=data['product_image_path'], 
                          product_price=data['product_price'],
                          product_cat_id=data['product_cat_id'])
    new_product.save()
    return jsonify({'message': 'Product added successfully'}), 201

def get_product(product_id):
    product = get_product_or_404(product_id)
    return jsonify(product.serialize())

def update_product(product_id):
    product = get_product_or_404(product_id)
    data = request.get_json()
    product.product_name = data['product_name']
    product.product_desc = data['product_desc']
    product.product_image_path = data['product_image_path']
    product.product_price = data['product_price']
    product.product_cat_id = data['product_cat_id']
    product.save()
    return jsonify({'message': 'Product updated successfully'})

def delete_product(product_id):
    product = get_product_or_404(product_id)
    product.delete()
    return jsonify({'message': 'Product deleted successfully'})

def get_product_or_404(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        jsonify({'message': 'Product not found'}), 404
    return product
