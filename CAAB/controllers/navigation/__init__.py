from flask import Blueprint

navigator_bp = Blueprint('navigator', __name__)

from . import navigator