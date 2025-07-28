from CAAB.db import db
from datetime import datetime

class Mandatos(db.Model):
    __tablename__ = 'mandato'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mandato_values = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.Integer, nullable=True)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    modified_by = db.Column(db.Integer, nullable=True)
    modified_date = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return{
            "id" : self.id,
            "mandato_values" : self.mandato_values
        }
    
class Tipo(db.Model):
    __tablename__ = 'tipo'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_values = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.Integer, nullable=True)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    modified_by = db.Column(db.Integer, nullable=True)
    modified_date = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return{
            "id" : self.id,
            "tipo_values" : self.tipo_values
        }
    
class Categoria(db.Model):
    __tablename__ = 'categoria'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    categoria_values = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.Integer, nullable=True)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    modified_by = db.Column(db.Integer, nullable=True)
    modified_date = db.Column(db.DateTime, nullable=True)
    
    def to_dict(self):
        return{
            "id" : self.id,
            "categoria_values" : self.categoria_values
        }
    

class Status(db.Model):
    __tablename__ = 'table_status'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Status_values = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.Integer, nullable=True)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    modified_by = db.Column(db.Integer, nullable=True)
    modified_date = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return{
            "id" : self.id,
            "Status_values" : self.Status_values
        }
    
class Language(db.Model):
    __tablename__ = 'select_language'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Language_values = db.Column(db.String(255), nullable=True)
    language_code = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.Integer, nullable=True)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    modified_by = db.Column(db.Integer, nullable=True)
    modified_date = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return{
            "id" : self.id,
            "Language_values" : self.Language_values
        }