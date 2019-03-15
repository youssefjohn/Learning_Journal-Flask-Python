"""This is my file for my models. They are created using FLASKALCHEMY and they
   also have login functionality due to inheriting from the UserMixin class.
"""

from Learning_Journal import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

import datetime


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    """This is the User Model/Table. It has a relationship with the journal_entry Model"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(250))

    table_relationship = db.relationship("Journal_Entry", backref="author", lazy=True)


    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """This is a method on the User Model. When ran, it checks the hashed password
           that is stored in the database, against the password the user is trying to
           log in with.
        """
        return check_password_hash(self.password_hash, password)


class Journal_Entry(db.Model, UserMixin):
    """This is my journals Model/table. It has a relationship with the user table/model"""
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    time_spent = db.Column(db.Integer)
    what_i_learned = db.Column(db.Text)
    resources_to_remember = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, title, date, time_spent, what_i_learned, resources_to_remember, owner_id):
        self.title = title
        self.date = date
        self.time_spent = time_spent
        self.what_i_learned = what_i_learned
        self.resources_to_remember = resources_to_remember
        self.owner_id = owner_id

