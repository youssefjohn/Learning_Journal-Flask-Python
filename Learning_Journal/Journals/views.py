from Learning_Journal import db, app, login_manager
from Learning_Journal.models import Journal_Entry
from Learning_Journal.Journals.forms import JournalForm
from Learning_Journal.models import Journal_Entry
from flask_login import login_required, login_user, logout_user, current_user

from flask import Blueprint, redirect, render_template, request, url_for, flash


journal_blueprint = Blueprint('journal_blueprint', __name__)


#read
@journal_blueprint.route("/details")
@login_required
def details():
    journals = Journal_Entry.query.all()
    return render_template("detail.html", journals=journals)



#create
@journal_blueprint.route("/entry", methods=["GET", "POST"])
@login_required
def add_edit():
    form = JournalForm()



    if form.validate_on_submit():
        new_journal = Journal_Entry(title=form.title.data,
                                    date=form.date.data,
                                    time_spent=form.time_spent.data,
                                    what_i_learned=form.what_i_learned.data,
                                    resources_to_remember=form.resources_to_remember.data,
                                    owner_id=current_user.id)

        db.session.add(new_journal)
        db.session.commit()

        return redirect(url_for("core_blueprint.index_page"))

    else:
        print("h")
        print("FORM ERRORS: \n", form.errors)


    return render_template("new.html", form=form)


@journal_blueprint.route("/edit", methods = ["GET", "POST"])
@login_required
def update(blog_post_id):
    entry = Journal_Entry.query.get(blog_post_id)

    form = JournalForm()

    if form.validate_on_submit():




    return render_template("edit.html", form = form)




