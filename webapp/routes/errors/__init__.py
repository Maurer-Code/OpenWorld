from flask import Blueprint

errors = Blueprint('errors', __name__)

from webapp.routes.errors import handlers
