import requests
from flask import request, jsonify
from . import Dealer_bp
from flask_jwt_extended import jwt_required, get_jwt_identity

@Dealer_bp.route('/callMicroservice1', methods=['GET'])
@jwt_required()
def callMicroservice1():
    path = "http://localhost:7059/api/Values"
    token = request.authorization.token # or get_jwt_identity() if you just want the subject
    headers = {"Authorization": f"Bearer {token}",
               "Accept": "application/json"}
    resp = requests.post(path, headers=headers)
    if resp.status_code == 200:
        return "token verified"
    else:
        return "token failed"