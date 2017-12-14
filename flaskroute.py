from flask import Flask, render_template, request, flash, redirect, url_for,session, logging, request
from wtforms import Form, StringField,SelectField, RadioField,IntegerField, PasswordField, validators, TextField, TextAreaField,SubmitField
from wtforms.fields.html5 import DateField,EmailField
from passlib.hash import sha256_crypt
import firebase_admin
from firebase_admin import credentials, db
from regions import *
import User as use
import Contact as cont

cred = credentials.Certificate('cred/oopp-267d4-firebase-adminsdk-4rnbe-c9137365f3.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://oopp-267d4.firebaseio.com/'
})

app = Flask(__name__)
app.secret_key = 'shush'

userRefer = db.reference('userbase')
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
    name = StringField("Name",[validators.Length(min=4,max=50)])
    email = EmailField("Email",[validators.DataRequired(), validators.Email()])
    subject = StringField("Subject",[validators.Length(min=4, max=80)])
    message = TextAreaField("Message",[validators.Length(min=30)])

#@app.route('/contact', methods=['GET','POST'])
#def contact():
#    form = ContactForm()
#    if request.method == 'POST':
#        flash('Form Submitted!','success')
#        contact_db = root.child('contact_us')
#        contact_ = cont.Contact(name,email,subject,message)
#        contact_db.push({
#            'name': contact_.get_name(),
#            'email': contact_.get_email(),
#            'subject': contact_.get_subject(),
#            'message': contact_.get_message()
#        })
#    elif request.method == 'GET':
#        return render_template('contact.html',form=form)
#    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
