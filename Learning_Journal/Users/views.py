from Learning_Journal import db
from Learning_Journal.models import User
from Learning_Journal.Users.forms import LoginForm, RegistrationForm

from flask_login import login_required, login_user, logout_user
from flask import render_template, redirect, url_for, Blueprint


users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/register', methods=["GET", "POST"])
def register():
    """This is the register view. It creates a new User to input into the database"""

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:

            addition = User(name=form.name.data,
                            email=form.email.data,
                            password=form.password.data)

            db.session.add(addition)
            db.session.commit()

            return redirect(url_for("users_blueprint.login"))

    return render_template("register.html", form=form)


@users_blueprint.route('/login', methods=["GET", "POST"])
def login():
    """This is the login view. It allows the user to log in, it checks
       the email the user has provided, against the emails in the database.
       If there is a match, the user is logged in, and is able to make a post
    """
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
    """This is the logout function. If the user clicks on logout in the navigation bar,
       the user loses the rights to create a post.
    """
    logout_user()
    return redirect(url_for("core_blueprint.index_page"))
