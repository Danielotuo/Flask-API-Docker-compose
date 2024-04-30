from flask import Blueprint, request, jsonify, make_response
from .models import Product, db

# Blueprint for handling product routes
routes_bp = Blueprint('routes', __name__)


@routes_bp.route('/', methods=['GET'])
def test():
    """
    This is a test route.
    """
    return make_response(jsonify({'message': 'testing route'}), 200)


@routes_bp.route('/products', methods=['POST'])
def create_product():
    """
    Creates a new product.

    This function expects a JSON payload with 'name' and 'price' fields.
    It creates a new Product instance and adds it to the database.
    """
    try:
        data = request.get_json()
        new_product = Product(name=data['name'], price=data['price'])
        db.session.add(new_product)
        db.session.commit()
        return make_response(jsonify({'message': 'product added'}), 201)
    except Exception as e:
        return make_response(jsonify({'message': 'error adding product', 'error': str(e)}), 500)


@routes_bp.route('/products', methods=['GET'])
def get_products():
    """
    Retrieves all products.

    This function queries the database for all Product instances and returns them as a JSON array.

    """
    try:
        products = Product.query.all()
        return make_response(jsonify([product.serialize() for product in products]), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'error retrieving products', 'error': str(e)}), 500)


@routes_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    """
    Retrieves a single product by ID.
    This function queries the database for a Product instance with the specified ID and returns it as a JSON object. 
    """
    try:
        product = Product.query.filter_by(id=id).first()
        if product:
            return make_response(jsonify({'product': product.serialize()}), 200)
        return make_response(jsonify({'message': 'product not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error retrieving product', 'error': str(e)}), 500)
