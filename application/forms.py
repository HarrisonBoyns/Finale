from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, url, Email, Length
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField

class EmailClass(FlaskForm):
    name = StringField("Name", validators=[
        DataRequired(), Length(2, 50)])
    email = StringField("Email ", validators=[
        DataRequired(), Email()
        ])
    number = StringField("Number", validators=[
        DataRequired(), Length(7, 12)
        ])
    msg = StringField("Message", validators=[
        DataRequired(), Length(10, 1000)
        ]) 
    submit = SubmitField("Send Email")
