from flask import Blueprint

program = Blueprint('program', __name__, url_prefix='/program')

from webapp.routes.program import routes
