from flask import Blueprint
from app.controllers.customer import CustomerController
from app.controllers.product import ProductController
from app.controllers.order import OrderController
from app.controllers.worker import WorkerController

api = Blueprint('api', __name__)

@api.route('/customer/register', methods=['POST'])
def register_customer():
    return CustomerController().register()

@api.route('/product', methods=['POST'])
def create_product():
    return ProductController().create()

@api.route('/product', methods=['GET'])
def get_products():
    return ProductController().get_all()

@api.route('/order', methods=['POST'])
def create_order():
    return OrderController().create()

@api.route('/order', methods=['GET'])
def get_orders():
    return OrderController().get_all()

@api.route('/worker', methods=['POST'])
def create_worker():
    return WorkerController().create()

@api.route('/worker', methods=['GET'])
def get_workers():
    return WorkerController().get_all()
