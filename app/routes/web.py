from flask import Blueprint
from app.controllers.customer import CustomerController

web = Blueprint('web', __name__)

@web.route('/customer/register', methods=['POST'])
def register_customer():
    return CustomerController().register()
