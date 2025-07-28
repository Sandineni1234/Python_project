from CAAB.db import db

class UserRoleMenus(db.Model):
    __tablename__ = 'userrolemenus'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userRoleMenuID = db.Column(db.String(10), nullable=False)
    isactive = db.Column(db.Boolean, default=True)
    menu_ids = db.Column(db.Text, nullable=False)
    CreatedBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    ModifiedBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    modified_date = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=True)
    created_by_user = db.relationship('User', foreign_keys=[CreatedBy])
    modified_by_user = db.relationship('User', foreign_keys=[ModifiedBy])

    def to_dict(self):{
        "id" : self.id,
        "userRoleMenuID" : self.userRoleMenuID,
        "menu_ids": self.menu_ids
    }

class Menus(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CreatedBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    ModifiedBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    StageID = db.Column(db.Integer, db.ForeignKey('stage.id'), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    isactive = db.Column(db.Boolean, default=True)
    name = db.Column(db.String(255), nullable=True)
    navigateurl = db.Column(db.String(255), nullable=True)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    modified_date = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=True)
    created_by_user = db.relationship('User', foreign_keys=[CreatedBy])
    modified_by_user = db.relationship('User', foreign_keys=[ModifiedBy])
    stage = db.relationship('Stage')

    def to_dict(self):
        return {
            "id": self.id,
            # "Description": self.Description,
            # "Isactive": self.Isactive,
            # "Name": self.Name,
            "Navigateurl": self.Navigateurl,
            "StageID": self.StageID,
            # "CreatedBy": self.CreatedBy,
            # "ModifiedBy": self.ModifiedBy,
            # "created_date": self.created_date,
            # "modified_date": self.modified_date
        }
