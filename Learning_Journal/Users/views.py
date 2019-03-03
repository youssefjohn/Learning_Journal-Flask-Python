from Learning_Journal import db, app, login_manager
from Learning_Journal.models import User
from Learning_Journal.Users.forms import LoginForm, RegistrationForm

from flask_login import login_required, login_user, logout_user, current_user
from flask import request, render_template, redirect, url_for, flash, Blueprint


users_blueprint = Blueprint('users_blueprint', __name__)



@users_blueprint.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:

            addition = User(name=form.name.data,
                            email=form.email.data,
                            password=form.password.data)

            db.session.add(addition)
            db.session.commit()

            return redirect(url_for("core_blueprint.index_page"))



    return render_template("register.html", form=form)


@users_blueprint.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)

            return redirect(url_for("core_blueprint.index_page"))



    return render_template("login.html", form=form)


@users_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("index.html")