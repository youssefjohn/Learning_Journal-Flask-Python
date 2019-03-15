"""This is my forms file. It is what will be displayed on"""

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, DateField, ValidationError, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo




class JournalForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    date = DateField("Date", format='%Y-%m-%d')
    time_spent = IntegerField("Time Spent", validators=[DataRequired()])
    what_i_learned = TextAreaField("What did you learn", validators=[DataRequired()])
    resources_to_remember = TextAreaField("Any resources", validators=[DataRequired()])
    submit = SubmitField("Submit")


