from CAAB.models.dropdowns import Mandatos, Tipo, Categoria, Status, Language
from . import dropdowns_bp
from flask import jsonify


@dropdowns_bp.route('/mandatos', methods=['GET'])
def get_mandatos(): 
    mandatos_list = [Mandatos.to_dict(mandato) for mandato in Mandatos.query.all()]
    return(jsonify(mandatos_list))

@dropdowns_bp.route('/tipos', methods=['GET'])
def get_tipos(): 
    tipo_list = [Tipo.to_dict(mandato) for mandato in Tipo.query.all()]
    return(jsonify(tipo_list))

@dropdowns_bp.route('/categorias', methods=['GET'])
def get_categorias():
    categroria_list = [Categoria.to_dict(categoria) for categoria in Categoria.query.all()]
    return categroria_list

@dropdowns_bp.route('/Status', methods=['GET'])
def get_status():
    stauts_list = [Status.to_dict(status) for status in Status.query.all()]
    return stauts_list

@dropdowns_bp.route('/languages', methods=['GET'])
def get_languages():
    language_list = [Language.to_dict(language) for language in Language.query.all()]
    return(jsonify(language_list))