# seed.py
from app import create_app, db
from app.models import Product, User

print("Starting the seed script...")

app = create_app()

with app.app_context():
    # Create tables (if they don't exist)
    db.create_all()

    # Optional: Clear existing data (careful in real life!)
    Product.query.delete()
    User.query.delete()

    # Add some seed products
    product1 = Product(name='Gin Classic', price=25.5, description='Smooth taste gin.', image_url='https://example.com/gin1.jpg')
    product2 = Product(name='Gin Special', price=35.0, description='Limited edition gin.', image_url='https://example.com/gin2.jpg')

    # Add a test user (optional)
    test_user = User(name='testuser', email='test@example.com', password='password123')

    # Add to session and commit
    db.session.add_all([product1, product2, test_user])
    db.session.commit()

    print("Database seeded!")
