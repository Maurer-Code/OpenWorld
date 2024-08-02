

from webapp import app


def register_blueprints():

    from webapp.routes.program import program as program_blueprint
    app.register_blueprint(program_blueprint)

    from webapp.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from webapp.routes.errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)

    from webapp.routes.docs import docs as docs_blueprint
    app.register_blueprint(docs_blueprint)

