from flask import Blueprint

dropdowns_bp = Blueprint('dropdowns_bp', __name__)

from . import get_dropdowns