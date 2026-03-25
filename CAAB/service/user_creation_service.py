from datetime import datetime
from CAAB.models import User, Department
from CAAB.models.user_roles import UserRoleMenus
from CAAB.db import db
from CAAB.utils.response_enum import StatusCode, ResponseMessage


def create_user(user_data: dict):
    existing_user = User.query.filter_by(email=user_data.get("email")).first()
    if existing_user:
        return {"status": StatusCode.CONFLICT, "message": ResponseMessage.USER_EXISTS}

    try:
        department_id = get_department_id(user_data.get("department_id"))
        user_menu_id = get_user_menu_id(user_data.get("userMenuID"))

        new_user = User(
            username=user_data.get("email"),
            password=user_data.get("password"),
            isactive=1,
            created_date=datetime.now(),
            modified_date=datetime.now(),
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            email=user_data.get("email"),
            phone=user_data.get("phone"),
            created_by=None,
            modified_by=None,
            department_id=department_id,
            userMenuID=user_menu_id
        )

        db.session.add(new_user)
        db.session.commit()
        return {"status": StatusCode.SUCCESS, "message": ResponseMessage.USER_CREATED}

    except ValueError as ve:
        db.session.rollback()
        return {"status": StatusCode.NOT_FOUND, "message": str(ve)}

    except Exception:
        db.session.rollback()
        return {"status": StatusCode.SERVER_ERROR, "message": ResponseMessage.SERVER_ERROR}


def get_department_id(department_id: int):
    department = Department.query.filter_by(id=department_id).first()
    if not department:
        raise ValueError(ResponseMessage.DEPARTMENT_NOT_FOUND)
    return department.id


def get_user_menu_id(user_menu_id: int):
    role = UserRoleMenus.query.filter_by(id=user_menu_id).first()
    if not role:
        raise ValueError(ResponseMessage.USERMENU_NOT_FOUND)
    return role.id
