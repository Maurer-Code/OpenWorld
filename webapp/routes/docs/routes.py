from webapp.routes.docs import docs
from flask import render_template
from flask_login import current_user


@docs.route('/index')
def index():
    return render_template('docs/index.html', user=current_user)
