from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Order, OrderItem, Product, User
from sqlalchemy import func
from app.extensions import db
from app.routes.decorators import admin_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/orders')
@login_required
@admin_required
def admin_orders():
    if not current_user.is_admin:
        flash("Unathorized access.", "error")
        return redirect(url_for('main.index'))
    
    orders = Order.query.order_by(Order.id.desc()).all()
    return render_template('admin_orders.html'
    , orders=orders)

@admin_bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    total_orders = Order.query.count()
    total_products = Product.query.count()
    total_users = User.query.count()

    total_revenue = db.session.query(
        func.sum(OrderItem.unit_price * OrderItem.quantity)
    ).scalar() or 0

    # Last five order
    recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()

    return render_template('admin/dashboard.html',
                            total_orders=total_orders,
                            total_products=total_products,
                            total_users=total_users,
                            total_revenue=total_revenue,
                            recent_orders=recent_orders)