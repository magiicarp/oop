from wtforms import Form, StringField,SelectField, RadioField,IntegerField, PasswordField, validators, TextField, TextAreaField,SubmitField
from wtforms.fields.html5 import DateField,EmailField
from passlib.hash import sha256_crypt

#REGISTER FORM
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    age = IntegerField('Age',[validators.NumberRange(min=10,max=120)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

#OONTACT FORM
class ContactForm(Form):
    name = StringField('Name',[validators.Length(min=1, max=50)])
    email = StringField('Email',[validators.Length(min=4, max=60)])
    subject = StringField('Subject')
    message = TextAreaField('Message')
    submit = SubmitField('Send')