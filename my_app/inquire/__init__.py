from flask import Blueprint

inquire = Blueprint('inquire', __name__)

from . import inquire_view, errors