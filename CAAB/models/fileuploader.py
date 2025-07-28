from CAAB.db import db

class FileUploader(db.Model):
    __tablename__ = 'FileUploader'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DealersID = db.Column(db.Integer, db.ForeignKey('Dealers.id'), nullable=False)
    FilePath = db.Column(db.String(500))
    filename = db.Column(db.String(255))
    stageID = db.Column(db.Integer, db.ForeignKey('stage.id'), nullable=False)
    CreatedBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ModifiedBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    Created_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=True)
    Modified_date = db.Column(db.DateTime, nullable=True)
    isactive = db.Column(db.Boolean, nullable=False)
    DocumentID = db.Column(db.Integer, db.ForeignKey('documents.id_doc'), nullable=False)

    Documents = db.relationship('Documents')
    # created_by = db.relationship('User', foreign_keys=[CreatedBy])
    # modified_by = db.relationship('User', foreign_keys=[ModifiedBy])
    # stage = db.relationship('Stage', backref='Dealer')

    def to_dict(self):
        return {
            # "id": self.id,
            # "DealersID": self.DealersID,
            "FilePath": self.FilePath,
            "filename": self.filename,
            "DocumentID" : self.Documents.to_dict() if self.Documents else None,
            # "stageID": self.stageID,
            # "CreatedBy": self.CreatedBy,
            # "ModifiedBy": self.ModifiedBy,
            # "Created_date": self.Created_date,
            # "Modified_date": self.Modified_date,
            # "isactive": self.isactive
        }

class Documents(db.Model):
    __tablename__ = 'documents'

    id_doc = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(50), nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=True)
    modified_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    modified_date = db.Column(db.DateTime, nullable=True)
    isactive = db.Column(db.Boolean, nullable=False, default=True)

    def to_dict(self):
        return {
            "id_doc": self.id_doc,
            "Name": self.Name,
            # "created_by": self.created_by,
            # "created_date": self.created_date.isoformat() if self.created_date else None,
            # "modified_by": self.modified_by,
            # "modified_date": self.modified_date.isoformat() if self.modified_date else None,
            # "isactive": self.isactive
        }