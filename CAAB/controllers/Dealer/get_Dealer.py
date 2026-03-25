from flask import request, jsonify
from . import Dealer_bp
from flask_jwt_extended import jwt_required
from CAAB.utils.common import parse_int
from CAAB.middlewares import logger
from CAAB.service import dealer_service

@Dealer_bp.route('/get_dealer', methods=['GET'])
@jwt_required()
def get_Dealer():
        dealer_id = parse_int(request.args.get('DealerID'))
        if not dealer_id:
            return jsonify({"error": "DealerID is required"}), 400

        try :
            dealer_data = dealer_service.get_dealer_full_details(dealer_id)
            if not dealer_data:
                return jsonify({"error": "Dealer not found"}), 404

            return jsonify(dealer_data), 200
        except Exception as e:
            logger.exception("Error fetching dealer details: %s", str(e))
            return jsonify({"error": str(e)}), 500 