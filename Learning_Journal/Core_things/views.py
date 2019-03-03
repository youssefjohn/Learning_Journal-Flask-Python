from flask import Flask, render_template, url_for, flash, redirect, Blueprint
from Learning_Journal import app, db
from Learning_Journal.models import Journal_Entry

core_blueprint = Blueprint('core_blueprint', __name__)

@core_blueprint.route('/')
def index_page():
    return render_template("home.html")



@core_blueprint.route('/entries')
def list_page():
    journals = Journal_Entry.query.all()
    return render_template("index.html", journals = journals)


