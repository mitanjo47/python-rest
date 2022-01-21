from flask import Flask
from config import Config as cfg
from app.controller.product_controller import ctrl_product
from app.controller.order_controller import ctrl_order

app = Flask(__name__)
app.register_blueprint(ctrl_product)
app.register_blueprint(ctrl_order)

@app.route(f"{cfg.API_URL}")
def index():
     return "Welcome to the default url"