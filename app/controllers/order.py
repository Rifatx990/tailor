from flask import request, jsonify
from app.models.order import Order

class OrderController:
    def create(self):
        customer_id = request.json['customer_id']
        order_date = request.json['order_date']
        total = request.json['total']
        order = Order(customer_id, order_date, total)
        order.save()
        return jsonify({'message': 'Order created successfully'}), 201

    def get_all(self):
        cursor = db.cursor()
        query = "SELECT * FROM orders"
        cursor.execute(query)
        orders = cursor.fetchall()
        cursor.close()
        return jsonify([{'id': order[0], 'customer_id': order[1], 'order_date': order[2], 'total': order[3]} for order in orders]), 200
