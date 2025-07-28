from CAAB.db import db
from datetime import datetime

class CommentsIncidents(db.Model):
    __tablename__ = 'CommentsIncidents'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DealersID = db.Column(db.Integer, db.ForeignKey('Dealers.id'), nullable=False)
    Comments = db.Column(db.String(255))
    Incidents = db.Column(db.String(255))
    stageID = db.Column(db.Integer, db.ForeignKey('stage.id'), nullable=False)
    CreatedBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ModifiedBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    Created_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    Modified_date = db.Column(db.DateTime, nullable=True)
    isactive = db.Column(db.Boolean, nullable=False)

    Dealers = db.relationship('Dealers', backref='CommentsIncidents')
    stage = db.relationship('Stage', backref='Dealers')
    created_by_user = db.relationship('User', foreign_keys=[CreatedBy])
    modified_by_user = db.relationship('User', foreign_keys=[ModifiedBy])

    def to_dict(self):
        return {
            # "id": self.id,
            # "DealersID": self.DealersID,
            "Comments": self.Comments,
            "Incidents": self.Incidents,
            # "stageID": self.stageID,
            # "CreatedBy": self.CreatedBy,
            # "ModifiedBy": self.ModifiedBy,
            # "Created_date": self.Created_date,
            # "Modified_date": self.Modified_date,
            # "isactive": self.isactive
        }
