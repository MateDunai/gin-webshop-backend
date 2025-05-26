from flask import Blueprint, jsonify, request, abort
from app.models import Product
from app import db

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/', methods=['GET'])
def get_products():
    return jsonify({'message': 'Product list will go here'})