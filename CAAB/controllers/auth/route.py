from flask import jsonify, request
from CAAB.models.user import User
from . import login
import bcrypt
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, get_jwt_identity, jwt_required
import jwt
import datetime
import os

@login.route("/Login", methods=['POST'])
def authenticate_User():
    data = request.get_json()
    access_token_expire = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES"))
    refresh_token_expire = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES"))
    password = data['Password']
    user = User.query.filter_by(email = data.get('Username')).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')) and user.isactive == True:
        jwt_token = generate_jwt_token(user)
        jwt_token_expire = int((datetime.datetime.now() + datetime.timedelta(minutes=access_token_expire)).timestamp())
        refresh_token = generate_refresh_token(user)
        jwt_refresh_token = int((datetime.datetime.now() + datetime.timedelta(days=refresh_token_expire)).timestamp())
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
    

def generate_jwt_token(user):
    return create_access_token(identity= str(user.id), additional_claims={
        'role': user.userMenuID,
        'department': user.department_id,
    })

def generate_refresh_token(user):
    return create_refresh_token(identity= str(user.id), additional_claims={
        'role': user.userMenuID,
        'department': user.department_id,
    })    