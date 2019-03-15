"""This is my views file for Core_things.
   It contains the main/home, views/pages for
   My app.
"""

from flask import Flask, render_template, Blueprint
from Learning_Journal.models import Journal_Entry

# Blueprint creation
core_blueprint = Blueprint('core_blueprint', __name__)


# Home page creation
@core_blueprint.route('/')
def index_page():
    return render_template("home.html")


# Entries page creation
@core_blueprint.route('/entries')
def list_page():
    """ This view collects all of the journal entries
        In the Database, then it displays them on the
        entries page.
    """
    journals = Journal_Entry.query.all()
    return render_template("index.html", journals = journals)


