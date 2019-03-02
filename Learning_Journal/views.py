from Learning_Journal import db, app, login_manager
from Learning_Journal.forms import JournalForm, RegistrationForm, LoginForm
from Learning_Journal.models import User, Journal_Entry

from flask_login import login_required, login_user, logout_user, current_user
from flask import request, render_template, redirect, url_for, flash



@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():

        if User.query.get(email=form.email.data):
            return redirect(url_for("register"))

        addition = User(name=form.name.data,
                        email=form.email.data,
                        password=form.password.data)


        return redirect(url_for("login"))




    return render_template("register.html", form=form)


# @app.route('/login', methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#
#     if form.validate_on_submit():
#         pass
#
#
#
#
#     return render_template()
#
#
#
# @app.route("/entry")
# def add_edit_page():
#     form = JournalForm()
#
#     if form.validate_on_submit():
#         #new_user= User(name=form.)
#         pass
#
#
# @app.route('details')
# def display_page():
#     pass