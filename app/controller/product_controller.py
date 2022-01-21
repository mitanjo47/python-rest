from flask_restx import Namespace, Resource, fields

api = Namespace('order', description='Product related operations')

order = api.model('Product', {
    'id': fields.Integer(required=True, description='The product identifier'),
    'name': fields.String(required=True, description='Napme of the product'),
    'description': fields.String(required=False, description='Description of the product'),
})

PRODUCTS = [
    {'id': 1, 'name': 'Product #1', 'description': 'Description of this product...'},
    {'id': 2, 'name': 'Product #2', 'description': 'Description of this product...'},
]

@api.route('/')
class ProductController(Resource):
    def get(self):
        return PRODUCTS