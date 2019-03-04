from Learning_Journal import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from flask_login import UserMixin


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

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
        return check_password_hash(self.password_hash, password)


class Journal_Entry(db.Model, UserMixin):
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
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










