from flask import request, jsonify
from app.models.product import Product

class ProductController:
    def create(self):
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        product = Product(name, description, price)
        product.save()
        return jsonify({'message': 'Product created successfully'}), 201

    def get_all(self):
        cursor = db.cursor()
        query = "SELECT * FROM products"
        cursor.execute(query)
        products = cursor.fetchall()
        cursor.close()
        return jsonify([{'id': product[0], 'name': product[1], 'description': product[2], 'price': product[3]} for product in products]), 200
