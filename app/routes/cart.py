from flask import Blueprint, session, redirect, url_for, request, flash, render_template
from app.models import Product
from app.extensions import db

cart_bp = Blueprint('cart', __name__, url_prefix='/cart')

@cart_bp.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    cart = session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    session['cart'] = cart
    flash('Product added to cart!', 'success')
    return redirect(request.referrer or url_for('main.index'))

@cart_bp.route('/')
def view_cart():
    cart = session.get('cart', {})
    product_ids = list(map(int, cart.keys()))

    products = Product.query.filter(Product.id.in_(product_ids)).all()

    cart_items = []
    total_price = 0

    for product in products:
        quantity = cart[str(product.id)]
        cart_items.append({
            'product': product,
            'quantity': quantity
        })
        total_price += product.price * quantity

    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@cart_bp.route('/updated/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    cart = session.get('cart', {})
    product_id_str = str(product_id)
    quantity = request.form.get('quantity', type=int)

    if quantity is None or quantity < 1:
        flash('Invalid quantity.', 'error')
        return redirect(url_for('cart.view_cart'))
    
    if product_id_str in cart:
        cart[product_id_str] = quantity
        session['cart'] = cart
        flash('Cart updated!', 'success')
    else:
        flash('Product not found in cart.', 'error')

    return redirect(url_for('cart.view_cart'))


@cart_bp.route('/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cart = session.get('cart', {})

    product_id_str = str(product_id)
    if product_id_str in cart:
        del cart[product_id_str]
        session['cart'] = cart
        flash('Product removed from cart!', 'success')
    else: 
        flash('Product not found in cart.', 'error')


    return redirect(url_for('cart.view_cart'))