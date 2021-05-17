from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, Email

class ContactForm(FlaskForm):
    name = StringField(
        validators=[Length(min=2, max=50, message='Minimum 2 characters Maxinmun 50')])
    email = StringField(validators=[Email(message="must be an email")])
    message = TextAreaField()



