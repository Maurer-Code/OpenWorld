from flask import Blueprint

docs = Blueprint('docs', __name__, url_prefix='/docs')

from webapp.routes.docs import routes
