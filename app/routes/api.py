from flask import Blueprint
from app.controllers.customer import CustomerController

api = Blueprint('api', __name__)

@api.route('/customer/register', methods=['POST'])
def register_customer():
    return CustomerController().register()
