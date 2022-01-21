from flask import Blueprint
from config import Config as cfg

CTRL_MAP = f"{cfg.API_URL}/order"
ctrl_order = Blueprint('order', __name__)

@ctrl_order.route(f"{CTRL_MAP}")
def index():
    return 'this is the index of order controller'

@ctrl_order.route(f"{CTRL_MAP}/test")
def test_action():
    return 'this is the test action of order controller'