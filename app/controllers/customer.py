from flask import request, jsonify
from app.models.customer import Customer

class CustomerController:
    def register(self):
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        phone = request.json['phone']
        customer = Customer(name, email, password, phone)
        customer.save()
        return jsonify({'message': 'Customer registered successfully'}), 201
