"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()

    return jsonify(members), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def get_one_member(member_id):
    member = jackson_family.get_member(member_id)

    if member is None:
        raise APIException("Member not found", status_code=400)

    return jsonify(member), 200

@app.route('/members', methods=['POST'])
def add_members():
    resp = request.json

     # Check if the required keys are present in the request
    required_keys = ['first_name', 'last_name', 'age', 'lucky_numbers']
    if not all(key in resp for key in required_keys):
        raise APIException("Invalid request data. Missing required keys.", status_code=400)

    new_member = jackson_family.add_member(resp)

    return jsonify("Jackson registered"), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    resp = request.json

    if not resp:
        raise APIException("Invalid request data", status_code=400)

    member = jackson_family.delete_member(member_id)

    return jsonify("Jackson deleted"), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)