import jwt
from flask import request, jsonify
from app.models.customer import Customer

def authenticate():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing'}), 401
    try:
        data = jwt.decode(token, 'secret_key_here', algorithms=['HS256'])
        customer = Customer.query.get(data['customer_id'])
        if not customer:
            return jsonify({'message': 'Invalid token'}), 401
        return customer
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401
