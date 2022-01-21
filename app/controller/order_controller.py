from flask_restx import Namespace, Resource, fields

api = Namespace('order', description='Order related operations')

order = api.model('Order', {
    'id': fields.Integer(required=True, description='The order identifier'),
    'name': fields.String(required=True, description='Description of the order'),
})

ORDERS = [
    {'id': 1, 'name': 'Order #1'},
]

@api.route('/')
class OrderController(Resource):
    def get(self):
        return ORDERS