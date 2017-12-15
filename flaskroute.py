from flask import Flask, render_template, request, flash, redirect, url_for,session, logging, request
from wtforms import Form, StringField,SelectField, RadioField,IntegerField, PasswordField, validators, TextField, TextAreaField,SubmitField
from wtforms.fields.html5 import DateField,EmailField
from passlib.hash import sha256_crypt
import firebase_admin
from firebase_admin import credentials, db
from regions import *
import User as use
import Contact as c
from flask_mail import Mail, Message


cred = credentials.Certificate('cred/oopp-267d4-firebase-adminsdk-4rnbe-c9137365f3.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://oopp-267d4.firebaseio.com/'
})

app = Flask(__name__)
app.secret_key = 'shush'
mail = Mail(app)

userRefer = db.reference('userbase')
#contactRefer = db.reference('contact')
root = db.reference()

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



@app.route('/')
def index():
    return render_template('index.html')

#USER REGISTER
@app.route('/register/', methods=["GET","POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data.title()
        age = form.age.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        user_db = root.child('userbase')
        user = use.User(name,username,age,email,password)
        user_db.push({
            'name': user.get_name(),
            'username': user.get_username(),
            'age': user.get_age(),
            'email': user.get_email(),
            'password': user.get_password()
        })
        flash('You have registered successfully', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

#LOGIN FORM
class Loginform(Form):
    un = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired])

#USER LOGIN
@app.route('/login',methods=['GET','POST'])
def login():
    form = Loginform(request.form)
    if request.method == 'POST' and form.validate():
        un = form.un.data
        password = sha256_crypt.encrypt(str(form.password.data))
        if ['username'] == id and ['password'] == password:
                session['logged_in'] = True
                session['id'] = id
                return redirect(url_for('index.html'))
        flash('Invalid username or password', 'danger')
        return render_template('login.html')

@app.route('/healthyeating')
def healthyeating():
    return render_template('eating.html')

@app.route('/planner')
def planner():
    return render_template('planner.html')

@app.route('/events')
def events():
    return render_template('events.html')
#CONTACT FORM
class ContactForm(Form):
    name = StringField('Your Name:', [validators.DataRequired()])
    email = StringField('Your e-mail address:', [validators.DataRequired(), validators.Email('your@email.com')])
    message = TextAreaField('Your message:', [validators.DataRequired()])
    submit = SubmitField('Send Message')

#@app.route('/contact', methods=['GET','POST'])
#def contact():
#    form = ContactForm()
#    if request.method == 'POST':
#        if form.validate() == False:
#            flash('Please fill in all fields','danger')
#            return render_template('contact.html',form=form)
#        else:
#            msg = Message("Hello" + form.name.data, recipients=['angelic.pen@gmail.com'])
#            msg.body = """
#                        From: %s <%s>,
#                        %s
#                        """ % (form.name.data, form.email.data, form.message.data)
#            mail.send(msg)
#            contact_db = root.child('contact')
#            contact_us = c.Contact()
#            contact_db.push({
#                'name': contact_us.get_name(),
#                'email': contact_us.get_email(),
#                'subject': contact_us.get_subject(),
#                'message': contact_us.get_message()
#            })
#            return "Successfully  sent message!"
#    elif request.method == 'GET':
#        return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
