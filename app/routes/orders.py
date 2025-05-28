from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.extensions import db
from app.models import Product, Order, OrderItem

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

@orders_bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            cart_items.append({'product': product,'quantity': quantity})
            total_price += product.price * quantity

    if request.method == 'POST':
        customer_name = request.form.get('name')
        customer_email = request.form.get('email')

        if not customer_name or not customer_email:
            flash("Please enter both name and email!", 'error')
            return render_template('checkout.html', cart_items=cart_items, total_price=total_price)
        
        order = Order(customer_name=customer_name, customer_email=customer_email)
        db.session.add(order)
        db.session.flush()

        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item['product'].id,
                quantity=item['quantity'],
                unit_price=item['product'].price
            )
            db.session.add(order_item)
        
        db.session.commit()
        session.pop('cart', None)
        flash("Order placed successfully!", 'success')
        return redirect(url_for('orders.confirmation'))
    
    return render_template('checkout.html', cart_items=cart_items, total_price=total_price)

@orders_bp.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')