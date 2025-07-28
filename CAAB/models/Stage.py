from CAAB.db import db

class Stage(db.Model):

    __tablename__ = 'stage'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Stage_name = db.Column(db.String(255), nullable=True)
    CreatedBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    ModifiedBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    modified_date = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return{
            "id" : self.id,
            "Stage_name" : self.Stage_name
        }