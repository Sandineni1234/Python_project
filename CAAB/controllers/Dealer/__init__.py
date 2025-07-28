from flask import Blueprint

Dealer_bp = Blueprint('Dealer_bp', __name__)

from . import create_dealers, get_Dealers_list, get_Dealer