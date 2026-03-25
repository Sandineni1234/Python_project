from flask import request, jsonify
from . import User_creation_bp
from CAAB.service import user_creation_service


@User_creation_bp.route("/User_Creation", methods=['POST'])
def user_creation():
    user_info = request.get_json()
    if not user_info:
        return jsonify({"message": "Invalid request body"}), 400

    result = user_creation_service.create_user(user_info)
    return jsonify({"message": result["message"]}), result["status"]
