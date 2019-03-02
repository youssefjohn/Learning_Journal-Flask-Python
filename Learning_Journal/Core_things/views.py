from flask import Flask, render_template, url_for, flash, redirect, Blueprint
from Learning_Journal import app, db


core_blueprint = Blueprint('core_blueprint', __name__)

@core_blueprint.route('/')
def index_page():
    return render_template("index.html")



