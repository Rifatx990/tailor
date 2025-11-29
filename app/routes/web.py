from flask import Blueprint
from app.controllers.customer import CustomerController
from app.controllers.product import ProductController
from app.controllers.order import OrderController
from app.controllers.worker import WorkerController

web = Blueprint('web', __name__)

@web.route('/customer/register', methods=['POST'])
def register_customer():
    return CustomerController().register()

@web.route('/product', methods=['POST'])
def create_product():
    return ProductController().create()

@web.route('/product', methods=['GET'])
def get_products():
    return ProductController().get_all()

@web.route('/order', methods=['POST'])
def create_order():
    return OrderController().create()

@web.route('/order', methods=['GET'])
def get_orders():
    return OrderController().get_all()

@web.route('/worker', methods=['POST'])
def create_worker():
    return WorkerController().create()

@web.route('/worker', methods=['GET'])
def get_workers():
    return WorkerController().get_all()
