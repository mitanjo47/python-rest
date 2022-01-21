from flask import Blueprint
from config import Config as cfg

CTRL_MAP = f"{cfg.API_URL}/product"
ctrl_product = Blueprint('product', __name__)

@ctrl_product.route(f"{CTRL_MAP}")
def index():
    return 'this is the index of product controller'

@ctrl_product.route(f"{CTRL_MAP}/test")
def test_action():
    return 'this is the test() action of product controller'