"""This is my views file for Journals.
   It contains the ability to, create, read, update and delete,
   for my app.
"""

from Learning_Journal import db
from Learning_Journal.models import Journal_Entry
from Learning_Journal.Journals.forms import JournalForm
from Learning_Journal.models import Journal_Entry, User
from flask_login import login_required, current_user

from flask import Blueprint, redirect, render_template, url_for


journal_blueprint = Blueprint('journal_blueprint', __name__)


#read
@journal_blueprint.route("/details")
@login_required
def details():
    """This is my read view. It sends all of the journal entries into a variable list
       Then it send the list to the details template.
    """

    journals = Journal_Entry.query.all()
    return render_template("detail.html", journals=journals)



#create
@journal_blueprint.route("/entry", methods=["GET", "POST"])
@login_required
def add():
    """This is my add view. It adds new entries into the database after
       The user has completed the form on the new.html template.
    """
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
        print("FORM ERRORS: \n", form.errors)

    return render_template("new.html", form=form)






@journal_blueprint.route("/entries/edit/<int:journal_post_id>", methods = ["GET", "POST"])
@login_required
def update(journal_post_id):
    """This is my journal update view. Once the form is completed on the template page
       The view looks for the entry that matches the same ID. Once it has a match,
       It begins putting new values into that entries coloumns.
    """
    form = JournalForm()
    entry = Journal_Entry.query.filter_by(id=journal_post_id).first()
    if entry.owner_id == current_user.id:

        if form.validate_on_submit():
            entry.title = form.title.data
            entry.date = form.date.data
            entry.time_spent = form.time_spent.data
            entry.what_i_learned = form.what_i_learned.data
            entry.resources_to_remember = form.resources_to_remember.data
            entry.owner_id = current_user.id

            db.session.add(entry)
            db.session.commit()

            return redirect(url_for("journal_blueprint.details"))
    else:
        return redirect(url_for("journal_blueprint.details"))

    return render_template("edit.html", form = form)


@journal_blueprint.route("/entries/delete/<int:journal_post_id>", methods=["GET", "POST"])
@login_required
def delete_post(journal_post_id):
    """This is my delete view. Just like the update view, it takes the ID of the,
       entry that the user is trying to delete on the details view/page.
       It then matches the ID to the entry in the database. Once a match is found,
       a deletion occurs and then the user is redirected to the index page.
    """
    entry = Journal_Entry.query.filter_by(id=journal_post_id).first()

    if entry.owner_id != current_user.id:
        return redirect(url_for("journal_blueprint.details"))

    db.session.delete(entry)
    db.session.commit()

    return redirect(url_for("core_blueprint.index_page"))




