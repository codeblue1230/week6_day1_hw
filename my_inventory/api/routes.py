from flask import Blueprint, request, jsonify
from my_inventory.helpers import token_required
from my_inventory.models import db, Lego, lego_schema, legos_schema

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/getdata')
def getdata():
    return{'some': 'value'}

# Create 1 Endpoint
@api.route('/legos', methods = ['POST'])
@token_required
def create_lego(my_user):

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    difficulty = request.json['difficulty']
    piece_count = request.json['piece_count']
    lego_category = request.json['lego_category']
    user_token = my_user.token

    print(f"User Token: {my_user.token}")

    lego = Lego(name, description, price, difficulty, piece_count, lego_category, user_token)

    db.session.add(lego)
    db.session.commit()

    response = lego_schema.dump(lego)

    return jsonify(response)

# Read 1 Endpoint
@api.route('/legos/<id>', methods = ['GET'])
@token_required
def get_lego(my_user, id):
    if id:
        lego = Lego.query.get(id)
        response = lego_schema.dump(lego)
        return jsonify(response)
    else:
        return jsonify({'message': 'ID is missing'}), 401
    
# Read all lego sets
@api.route('/legos', methods = ['GET'])
@token_required
def get_legos(my_user):
    token = my_user.token
    legos = Lego.query.filter_by(user_token = token).all()
    response = legos_schema.dump(legos)

    return jsonify(response)

# Update 1 lego set by ID
@api.route('/legos/<id>', methods = ["PUT"])
@token_required
def update_lego(my_user, id):
    lego = Lego.query.get(id)

    lego.name = request.json['name']
    lego.description = request.json['description']
    lego.price = request.json['price']
    lego.difficulty = request.json['difficulty']
    lego.piece_count = request.json['piece_count']
    lego.lego_category = request.json['lego_category']
    lego.user_token = my_user.token

    db.session.commit()

    response = lego_schema.dump(lego)

    return jsonify(response)

# Delete 1 Lego set by ID
@api.route('/legos/<id>', methods = ['DELETE'])
@token_required
def delete_lego(my_user, id):
    lego = Lego.query.get(id)

    db.session.delete(lego)
    db.session.commit()

    response = lego_schema.dump(lego)

    return jsonify(response)