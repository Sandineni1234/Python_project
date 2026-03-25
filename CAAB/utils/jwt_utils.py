from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import datetime, timezone
from CAAB.middlewares import logger

def _build_claims(user):
    if user.userMenuID and user.department_id:
        return {
           'role': user.userMenuID,
            'department': user.department_id,
        }
    else:
        return {
            'role': "",
            'department': "",
        }    

def generate_jwt_token(user):
    return create_access_token(identity=str(user.id), additional_claims=_build_claims(user))

def generate_refresh_token(user):
    return create_refresh_token(identity=str(user.id), additional_claims=_build_claims(user))

def powerBI_jwt_token(userId):
    return create_access_token(identity=str(userId), additional_claims={
        'Permission': "admin",
        'Client' : "BVVA"
    })