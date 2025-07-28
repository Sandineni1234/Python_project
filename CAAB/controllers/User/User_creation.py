from flask import request, jsonify
from CAAB.models import User
from CAAB.models import Department
from CAAB.models.user_roles import UserRoleMenus
from . import User_creation_bp
from datetime import datetime, date
from CAAB.db import db

@User_creation_bp.route("/User_Creation", methods=['POST'])
def user_creation():
    User_info = request.get_json()
    get_user_email = User_info.get('email')
    check_email_exists = User.query.filter_by(email = get_user_email).first()
    if(check_email_exists is not None):
        return jsonify({'message': 'user already exist'}), 409
    if(check_email_exists is None):
        try:
            new_user = User(
                username = User_info["email"], 
                password = User_info["password"],
                isactive = 1,
                created_date = datetime.now(),
                modified_date = datetime.now(),
                first_name = User_info["first_name"],
                last_name = User_info["last_name"],
                email = User_info["email"],
                phone = User_info["phone"],
                created_by = None,
                modified_by = None,
                department_id = get_department_ID(User_info),
                userMenuID = get_userMenuID(User_info)
                )
            
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error:", e)
    return(jsonify({'message':'New user Created'}), 200)
# def get_creator_ID(self):
#     userID = User.query.filter_by(id = self.get("")).first()
#     return userID
# get_creator_ID(User_info)

def get_department_ID(self):
    deparment = Department.query.filter_by(id = self.get('department_id')).first()
    department_detials = Department.to_dict(deparment)
    print(department_detials)
    return department_detials["id"]

def get_userMenuID(self):
    UserRole_detials = UserRoleMenus.to_dict(UserRoleMenus.query.filter_by(id = self.get("userMenuID")).first())
    return UserRole_detials["id"]