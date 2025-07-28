from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from CAAB.models.user import User
from CAAB.models.user_roles import UserRoleMenus
from CAAB.models.user_roles import Menus
from CAAB.db import db

def check_menu_access(menu_id_param_name='menu_id'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_user = User.query.get(get_jwt_identity())
            if not current_user or not current_user.Isactive:
                return jsonify({"error": "Unauthorized"}), 403

            role_entry = UserRoleMenus.query.filter_by(
                userMenuID=current_user.userMenuID,
                isactive=True
            ).first()

            if not role_entry:
                return jsonify({"error": "Role not found or inactive"}), 403

            allowed_menu_ids = [int(mid.strip()) for mid in role_entry.menu_ids.split(',') if mid.strip().isdigit()]
            
            # Get menu_id from request data
            data = request.get_json() or {}
            menu_id = data.get(menu_id_param_name)
            if not menu_id or int(menu_id) not in allowed_menu_ids:
                return jsonify({"error": "Access denied"}), 403

            return func(*args, **kwargs)
        return wrapper
    return decorator
