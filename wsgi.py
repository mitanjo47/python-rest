from flask import Flask
from flask_restx import Api
from config import Config as cfg

from app.controller.order_controller import api as ctrl_order
from app.controller.product_controller import api as ctrl_product

### Initialize routing
api = Api(
    title='API Rest (python)',
    version='1.0',
    description='A description',
    # All API metadatas
)

# Registering controller routes
api.add_namespace(ctrl_order, f"{cfg.API_URL}orders")
api.add_namespace(ctrl_product, f"{cfg.API_URL}products")

app = Flask(__name__)
api.init_app(app)

@app.route(f"{cfg.API_URL}")
def index():
     return "Welcome to the default url"
 
### Initialize DB
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from app.models import Product

from flask_migrate import Migrate
migrate = Migrate(app, db)