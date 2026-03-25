from CAAB.models.user import User
from CAAB.models.user_roles import UserRoleMenus, Menus
from CAAB.db import db


def get_navigation_url_for_user(user_id: int, stage_id: int):

    user = User.query.filter_by(id=user_id).first()
    if not user:
        return {"error": "Invalid user", "status": 404}

    role = UserRoleMenus.query.filter_by(id=user.userMenuID, isactive=True).first()
    if not role or not role.menu_ids:
        return {"error": "No access role assigned", "status": 403}

    allowed_menu_ids = [
        int(mid.strip()) for mid in role.menu_ids.split(",") if mid.strip().isdigit()
    ]
    if not allowed_menu_ids:
        return {"access": False, "message": "No menus assigned", "status": 403}

    menu = (
        db.session.query(Menus)
        .filter(
            Menus.id.in_(allowed_menu_ids),
            Menus.StageID == stage_id,
            Menus.isactive == True
        )
        .first()
    )

    if not menu:
        return {"access": False, "message": "Access denied", "status": 403}

    return {"access": True, "navigation_url": menu.navigateurl, "status": 200}
