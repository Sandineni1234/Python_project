from flask import jsonify, request
from CAAB.models.user import User
from . import login
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask import current_app
from datetime import datetime, timezone, timedelta
from CAAB.utils.jwt_utils import generate_jwt_token, generate_refresh_token, powerBI_jwt_token
from CAAB.utils.common import parse_int
from CAAB.middlewares.logger import logger

@login.route("/Login", methods=['POST'])
def authenticate_User():
        data = request.get_json()
        password = data['Password']
        access_token_expire = current_app.config["JWT_ACCESS_TOKEN_EXPIRES"]
        refresh_token_expire = current_app.config["JWT_REFRESH_TOKEN_EXPIRES"]
        user = User.query.filter_by(email = data.get('Username')).first()
        if user and User.check_password(user,password) and user.isactive == True:
            jwt_token = generate_jwt_token(user)
            jwt_token_expire = int((datetime.now() + access_token_expire).timestamp())
            refresh_token = generate_refresh_token(user)
            jwt_refresh_token = int((datetime.now() + refresh_token_expire).timestamp())
            response = {
                "user_data": User.to_dict(user),
                "access_token": jwt_token,
                "refresh_token": refresh_token,
                "access_token_expire": jwt_token_expire,
                "refresh_token_expire": jwt_refresh_token
            }
            return jsonify(response), 200    
        else:
            return jsonify({'message':'Invalid credentials'}), 401

@login.route("/refresh", methods=['POST'])
@jwt_required(refresh=True)
def refresh_jwt_token():
        identity = get_jwt_identity()
        user = User.query.filter_by(id = identity).first()
        if user.isactive == True :
            access_token = create_access_token(identity=identity)
            return jsonify(access_token=access_token)
        else :
            return jsonify({'message': 'user is not active'})
        
@login.route("/powerBI", methods=['GET'])
def powerBI_token():
    userId = parse_int(request.headers.get('userId'))
    try:
        if userId :
            # user = User.query.filter_by(id = userId).first()
            jwt_token = powerBI_jwt_token(userId)
            # refresh_token = generate_refresh_token(user)
            response = {
                "powerBI_access_token": jwt_token,
                # "refresh_token": refresh_token,
            }
            return jsonify(response), 200
        else:
            return jsonify({"Message":"Invalid token"}), 401
    except Exception as e:
        logger.exception("powerBI token generation failed: %s", str(e))
        return jsonify({"error": str(e)}), 401