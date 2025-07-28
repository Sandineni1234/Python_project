from flask import Blueprint

departments_dp = Blueprint('departments_bp', __name__)

from . import get_departments