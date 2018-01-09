from flask import Flask, render_template, request, flash, redirect, url_for,session, logging, request
from wtforms import Form, StringField,SelectField, RadioField,IntegerField, PasswordField, validators, TextField, TextAreaField,SubmitField
from wtforms.fields.html5 import DateField,EmailField
from passlib.hash import sha256_crypt
import firebase_admin
from firebase_admin import credentials, db
from Forms import RegisterForm
from regions import *
import User as use
import Contact as c


cred = credentials.Certificate('cred/oopp-267d4-firebase-adminsdk-4rnbe-c9137365f3.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://oopp-267d4.firebaseio.com/'
})

app = Flask(__name__)
app.secret_key = 'shush'

userRefer = db.reference('userbase')
#contactRefer = db.reference('contact')
root = db.reference()

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
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/healthyeating')
def healthyeating():
    return render_template('eating.html')

@app.route('/planner')
def planner():
    return render_template('planner.html')

@app.route('/events')
def events():
    return render_template('events.html')


if __name__ == '__main__':
    app.run(debug=True)
