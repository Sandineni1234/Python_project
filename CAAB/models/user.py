from CAAB.db import db
import bcrypt

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    isactive = db.Column(db.Boolean, nullable=False)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    modified_date = db.Column(db.DateTime, nullable=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.BigInteger, unique=True, nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    modified_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    userMenuID = db.Column(db.Integer, db.ForeignKey('userrolemenus.id'), nullable=False)
    role = db.relationship('UserRoleMenus', backref='users', foreign_keys=[userMenuID])
    department = db.relationship('Department', backref='users')

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "department" : self.department.name if self.department else None,
            "userMenuID" : self.role.id if self.role else None
        }

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))