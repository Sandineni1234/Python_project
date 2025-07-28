from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from CAAB.models.user import User
from CAAB.models.user_roles import UserRoleMenus, Menus 
from . import navigator_bp
from CAAB.db import db

@navigator_bp.route('/get-navigation-url', methods=['GET'])
@jwt_required()
def get_navigation_url():
    stage_id = request.args.get('StageId')

    # Get current user from JWT
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()

    if not user:
        return jsonify({"error": "Invalid user"}), 404

    # Get role mapping
    role = UserRoleMenus.query.filter_by(id=user.userMenuID, isactive=True).first()
    if not role:
        return jsonify({"error": "No access role assigned"}), 403

    # Parse menu_ids string -> list of ints
    allowed_menu_ids = [int(mid.strip()) for mid in role.menu_ids.split(",") if mid.strip().isdigit()]

    # Find menu with matching stage_id in allowed menus
    menu = db.session.query(Menus).filter(
    Menus.id.in_(allowed_menu_ids),
    Menus.StageID == stage_id,
    Menus.isactive == True
    ).first()

    if not menu:
        return jsonify({"access": False, "message": "Access denied"}), 403

    return jsonify({
        "access": True,
        "navigation_url": menu.navigateurl 
    })
