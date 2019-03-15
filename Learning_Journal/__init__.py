"""This is the __init__ file for the app. It handles all of the imports and general set ups.
   Our app is created here, the database and the blueprints are all setup here.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os

app = Flask(__name__)

app.config["SECRET_KEY"] = "mykey"
basedir = os.path.abspath((os.path.dirname(__file__)))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Login Manager set up
login_manager = LoginManager(app)

login_manager.init_app(app)

login_manager.user_loader("login")



#Blueprint registration

from Learning_Journal.Core_things.views import core_blueprint
app.register_blueprint(core_blueprint)


from Learning_Journal.Users.views import users_blueprint
app.register_blueprint(users_blueprint)


from Learning_Journal.Journals.views import journal_blueprint
app.register_blueprint(journal_blueprint)