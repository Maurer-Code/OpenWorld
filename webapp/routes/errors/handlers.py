from webapp.routes.errors import errors
from webapp import db
from flask import render_template, request


def wants_api_response():
    return request.accept_mimetypes['application/json'] >= \
        request.accept_mimetypes['text/html']


@errors.app_errorhandler(401)
def error_401(error):

    return render_template("error.html", error=error, code=401), 401


@errors.app_errorhandler(403)
def error_403(error):

    return render_template("error.html", error=error, code=403), 403


@errors.app_errorhandler(404)
def error_404(error):

    return render_template("error.html", error=error, code=404), 404


@errors.app_errorhandler(405)
def error_405(error):

    return render_template("error.html", error=error, code=405), 405


@errors.app_errorhandler(413)
def error_413(error):

    return render_template("error.html", error=error, code=413), 413


@errors.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()

    return render_template("error.html", error=error, code=500), 500
