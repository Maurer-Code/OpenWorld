from webapp import app
from flask import render_template
from flask_login import login_required, current_user

from webapp.database import User, Role


@app.route('/')
def index():
    return render_template('base.html', user=current_user)


@app.route('/admin')
def admin():
    return render_template('admin.html', user=current_user)


@app.route('/home')
def home():
    return render_template('home.html', user=current_user)


@app.route('/members', methods=['GET', 'POST'])
@login_required
def members():
    return render_template('members.html', user=current_user, members=User.query)


@app.route('/roles', methods=['GET', 'POST'])
@login_required
def roles():
    return render_template('roles.html', user=current_user, roles=Role.query.all())


@app.route('/profile/<int:id>', methods=['GET', 'POST'])
@login_required
def profile(id):
    item = User.query.filter_by(id=id).first_or_404()
    return render_template('profile.html', user=current_user, profile=item)


@app.route('/root', methods=['GET', 'POST'])
def root():

    return render_template('root.html', user=current_user)
