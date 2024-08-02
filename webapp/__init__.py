from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

from webapp.config import Config

import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os


app = None

db = SQLAlchemy()

mail = Mail()

login = LoginManager()
login.login_view = 'login'
login.login_message = 'Please log in to access this page.'


def create_app(debug=False):

    """Create an application."""

    global app
    app = Flask(__name__)
    app.debug = debug
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)
    login.init_app(app)

    from webapp.routes import register_blueprints
    register_blueprints()

    with app.app_context():
        db.create_all()

    if not app.debug and not app.testing:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])

            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()

            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'],
                subject='Webapp Failure',
                credentials=auth,
                secure=secure)

            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

        if not os.path.exists('logs'):
            os.mkdir('logs')

        file_handler = RotatingFileHandler('logs/webapp.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(
            logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Webapp startup')

    from webapp.database import User

    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

