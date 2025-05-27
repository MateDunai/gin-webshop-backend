from flask import Blueprint, jsonify, request, abort
from flask_login import current_user, login_required
from app.models import Product
from app import db

products_bp = Blueprint('products', __name__, url_prefix='/products')

products_bp.route('/', methods=['POST'])
@login_required
def create_product():
    if not current_user.is_authenticated:
        abort(401)

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description', '')
    image_url = data.get('image_url', '')

    if not name or price is None:
        abort(400, 'Missing required fields')

    new_product = Product(
        name=name,
        price=price,
        description=description,
        image_url=image_url
    )
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product created', 'id': new_product.id}), 201



@products_bp.route('/', methods=['GET'])
def get_products():
    query = Product.query

    name = request.args.get('name')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)

    # Apply filters
    if name:
        query = query.filter(Product.name.ilike(f'%{name}%'))
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)

    products = query.all()

    products_list = []
    for product in products:
        products_list.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'image_url': product.image_url
        })

    return jsonify(products_list)


@products_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description' : product.description,
        'price' : product.price,
    })

@products_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@login_required
def update_product(id):
    product = product.query.get_or_404(id)

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    image_url = data.get('image_url')

    if name:
        product.name = name
    if price is not None:
        product.price = price
    if description is not None: 
        product.description = description
    if image_url is not None:
        product.image_url = image_url
    
    db.session.commit()

    return jsonify({'message': 'Product updated', 'id': product.id})


@products_bp.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_product(id):
    product = Product.query.get_or_404(id)

    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product deleted', 'id': id})