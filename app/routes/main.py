from flask import Blueprint, render_template
from app.models import Product

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    products = Product.query.all()
    return render_template('products.html', products=products)