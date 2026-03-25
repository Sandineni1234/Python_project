from flask import jsonify, request
from . import Dealer_bp
from flask_jwt_extended import jwt_required, get_jwt_identity
from CAAB.service import dealer_service

@Dealer_bp.route('/Dealer_list', methods=['GET'])
@jwt_required()
def get_dealers():
    user_id = get_jwt_identity()
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    dealer_list = dealer_service.get_dealer_list_for_user(user_id, page, per_page)
    if dealer_list is None:
        return jsonify({"message": "Unauthorized"}), 403

    return jsonify({
        "Success": True,
        "Status": 200,
        "data": dealer_list,
        "Total": dealer_list.get("total_items")
    }), 200
