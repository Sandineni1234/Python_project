from CAAB.db import db
from datetime import datetime

class Dealers(db.Model):
    __tablename__ = "Dealers"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Address = db.Column(db.String(255))
    AskForPolicy = db.Column(db.Boolean, nullable=True)
    CategoryID = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=True)
    CEAReceived = db.Column(db.Boolean, nullable=True)
    Comercial = db.Column(db.String(255))
    CompanyID = db.Column(db.String(255))
    CreatedBy = db.Column(db.Integer, db.ForeignKey('user.id'))
    Creation_date = db.Column(db.DateTime)
    EconGroup = db.Column(db.String(255))
    email = db.Column(db.String(255))
    Isactive = db.Column(db.Boolean, nullable=True)
    LegalName = db.Column(db.String(255))
    MandateID = db.Column(db.Integer, db.ForeignKey('mandato.id'), nullable=True)
    ModifiedBy = db.Column(db.Integer, db.ForeignKey('user.id'))
    Municipality = db.Column(db.String(255))
    PartnerNameSurname1 = db.Column(db.String(255))
    PartnerNameSurname2 = db.Column(db.String(255))
    PartnerNameSurname3 = db.Column(db.String(255))
    PostalCode = db.Column(db.String(255))
    Province = db.Column(db.String(255))
    ShareholderNameSurname1 = db.Column(db.String(255))
    ShareholderNameSurname2 = db.Column(db.String(255))
    ShareholderNameSurname3 = db.Column(db.String(255))
    ShareholderPercentage1 = db.Column(db.String(255))
    ShareholderPercentage2 = db.Column(db.String(255))
    ShareholderPercentage3 = db.Column(db.String(255))
    PartnerPercentage1 = db.Column(db.String(255))
    PartnerPercentage2 = db.Column(db.String(255))
    PartnerPercentage3 = db.Column(db.String(255))
    StageId = db.Column(db.Integer, db.ForeignKey('stage.id'), nullable = False)
    statusID = db.Column(db.Integer, db.ForeignKey('table_status.id'), nullable=True)
    typeID = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=True)
    Zone = db.Column(db.String(255))
    created_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    modified_date = db.Column(db.DateTime)

    stage = db.relationship('Stage', backref='Dealer')
    status = db.relationship('Status', backref='Dealer')
    Mandate = db.relationship('Mandatos', backref='Dealer')
    Category =db.relationship("Categoria")
    type = db.relationship('Tipo')
    created_by_user = db.relationship('User', foreign_keys=[CreatedBy])
    modified_by_user = db.relationship('User', foreign_keys=[ModifiedBy])

    def get_dealer_details(self):
        return {
            "id": self.id,
            "Address": self.Address,
            "AskForPolicy": self.AskForPolicy,
            "CategoryID": self.Category.to_dict() if self.Category else None,
            "CEAReceived": self.CEAReceived,
            "Comercial": self.Comercial,
            "CompanyID": self.CompanyID,
            "CreatedBy": self.created_by_user.to_dict() if self.created_by_user else None,
            "Creation_date": self.Creation_date,
            "EconGroup": self.EconGroup,
            "StageId" : self.StageId,
            "email": self.email,
            "LegalName": self.LegalName,
            "MandateID": self.Mandate.to_dict() if self.Mandate else None,
            "ModifiedBy": self.modified_by_user.to_dict() if self.modified_by_user else None,
            "Municipality": self.Municipality,
            "PartnerNameSurname1": self.PartnerNameSurname1,
            "PartnerNameSurname2": self.PartnerNameSurname2,
            "PartnerNameSurname3": self.PartnerNameSurname3,
            "PostalCode": self.PostalCode,
            "Province": self.Province,
            "ShareholderNameSurname1": self.ShareholderNameSurname1,
            "ShareholderNameSurname2": self.ShareholderNameSurname2,
            "ShareholderNameSurname3": self.ShareholderNameSurname3,
            "ShareholderPercentage1": self.ShareholderPercentage1,
            "ShareholderPercentage2": self.ShareholderPercentage2,
            "ShareholderPercentage3": self.ShareholderPercentage3,
            "PartnerPercentage1": self.PartnerPercentage1,
            "PartnerPercentage2": self.PartnerPercentage2,
            "PartnerPercentage3": self.PartnerPercentage3,
            "typeID": self.type.to_dict() if self.type else None,
            "Zone": self.Zone,
            "StatusID": self.status.to_dict() if self.statusID else None
        }