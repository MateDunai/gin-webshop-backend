from flask import Blueprint, jsonify, request, abort
from app.models import Product
from app import db

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_list = []
    for product in products: 
        products_list.append({
        'id': product.id,
        'title': product.title,
        'description' : product.description,
        'price' : product.price
        })
    return jsonify(products_list)

@products_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({
        'id': product.id,
        'title': product.title,
        'description' : product.description,
        'price' : product.price,
    })