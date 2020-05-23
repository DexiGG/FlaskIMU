from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from social_news import db
from social_news.models import User, NewsItem
from social_news.users.forms import RegistrationForm, LoginForm
from social_news.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('login.html', form=form)

# register
# login
# logout
#
