from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import navigator_bp
from CAAB.service import navigator_service


@navigator_bp.route('/get-navigation-url', methods=['GET'])
@jwt_required()
def get_navigation_url():
    stage_id = request.args.get('StageId', type=int)
    if not stage_id:
        return jsonify({"error": "StageId is required and must be an integer"}), 400

    current_user_id = get_jwt_identity()

    result = navigator_service.get_navigation_url_for_user(current_user_id, stage_id)

    return jsonify({k: v for k, v in result.items() if k != "status"}), result.get("status", 200)
