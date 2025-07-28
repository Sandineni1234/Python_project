from CAAB.db import db
from datetime import datetime

class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=True)
    isactive = db.Column(db.Boolean, nullable=False)
    isactive = db.Column(db.Integer, nullable=True)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    modified_by = db.Column(db.Integer, nullable=True)
    modified_date = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return{
           "id" : self.id,
            "name" : self.name,
            "isactive" : self.isactive
        }