from webapp import db
from webapp.routes.auth import auth

from flask import redirect, url_for, render_template, flash
from flask_login import login_user, login_required, logout_user, current_user

from webapp.database import User, Role

from .forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from .email import send_password_reset_email


@auth.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('base'))

    form = LoginForm()
    if form.validate_on_submit():

        item = User.query.filter_by(email=form.email.data).first()

        if item:

            if item.check_password(form.password.data):

                flash('Logged in successfully!', category='success')
                login_user(user=item, remember=form.remember_me.data)

                return redirect(url_for('home'))

            else:
                flash('Incorrect password, try again.', category='error')

        else:
            flash('Email does not exist.', category='error')

    return render_template('auth/login.html', title='Sign In', form=form)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if current_user.is_authenticated:
        return redirect(url_for('base'))

    form = RegistrationForm()
    if form.validate_on_submit():

        # Todo init with start of application
        if Role.query.first() is None:
            db.session.add(Role(name='Systemadmin'))
            db.session.add(Role(name='User'))
            db.session.commit()

        # Make first person to admin and activate profile
        active = False
        if User.query.first() is None:
            active = True
            role = Role.query.filter_by(name='Systemadmin').first()
        else:
            role = Role.query.filter_by(name='User').first()

        item = User(
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            role=role,
            active=active)

        item.set_password(form.password.data)

        db.session.add(item)
        db.session.commit()

        flash('Account created!', category='success')
        if active:
            login_user(item, remember=active)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('auth.login'))

    return render_template(url_for('auth.sign_up'), user=current_user, form=form)


@auth.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('base'))

    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        item = User.query.filter_by(email=form.email.data).first()
        if item:
            send_password_reset_email(item)
            flash('Check your email for the instructions to reset your password')

        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html', title='Reset Password', form=form)


@auth.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    item = User.verify_reset_password_token(token)
    if not item:
        return redirect(url_for('base'))

    form = ResetPasswordForm()
    if form.validate_on_submit():

        item.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')

        return redirect(url_for('auth.login'))

    return render_template('auth/reset_password.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    flash('Logged out successfully.', category='error')
    logout_user()
    return redirect(url_for('auth.login'))


