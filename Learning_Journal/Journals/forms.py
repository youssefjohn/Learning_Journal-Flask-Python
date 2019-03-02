from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, DateTimeField, ValidationError, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo




class JournalForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    date = DateTimeField("Data", validators=[DataRequired()])
    time_spent = StringField("Time Spent", validators=[DataRequired()])
    what_i_learned = TextAreaField("What did you learn", validators=[DataRequired()])
    resources_to_remember = TextAreaField("Any resources", validators=[DataRequired()])


class EditJournalForm(FlaskForm):
    title = StringField("Edit: Title", validators=[DataRequired()])
    date = DateTimeField("Edit: Data", validators=[DataRequired()])
    time_spent = StringField("Edit: Time Spent", validators=[DataRequired()])
    what_i_learned = TextAreaField("Edit: What did you learn", validators=[DataRequired()])
    resources_to_remember = TextAreaField("Edit: Any resources", validators=[DataRequired()])
