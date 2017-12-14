from flask import Flask, render_template, request, flash, redirect, url_for,session, logging, request
from wtforms import Form, StringField,SelectField, RadioField, PasswordField, validators
from wtforms.fields.html5 import DateField,EmailField
from passlib.hash import sha256_crypt
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('cred/oopp-267d4-firebase-adminsdk-4rnbe-c9137365f3.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://oopp-267d4.firebaseio.com/'
})

app = Flask(__name__)
app.secret_key = 'shush'

root = db.reference()

regions = [('Alexandra'),('Aljunied'),('Ang Mo Kio'),('Ayer Rajah'),('Balestier'),('Bartley'),('Bedok'),('Bidadari'),('Bishan'),('Boon Lay'),('Bukit Batok'),('Bukit Panjang'),
           ('Bukit Timah'),('Buona Vista'),('Changi'),('Chinatown'),('Choa Chu Kang'),('Clementi'),('Commonwealth'),('East Coast'),('Eunos'),('Farrer Park'),('Hougang'),
           ('Jalan Besar'),('Joo Chiat'),('Jurong East'),('Jurong West'),('Kallang'),('Kembangan'),('Kent Ridge'),('Kim Seng'),('Kranji'),('Lentor'),('Lim Chu Kang'),
           ('Little India'),('Lorong Chuan'), ('MacPherson'),('Mandai'),('Marina Bay'),('Mount Faber'),('Mount Vernon'),('Newton'),('Novena'),
           ('Orchard Road'),('Outram'),('Pasir Panjang'),('Pasir Ris'),('Paya Lebar'),('Potong Pasir'),('Punggol'),('Queenstown'),('Raffles Place'),('River Valley'),
           ('Sembawang'),('Sengkang'),('Serangoon'),('Tampines'),('Tanjong Pagar'),('Telok Blangah'),('Tiong Bahru'),('Toa Payoh'),('Tuas'),('Woodlands'),('Yishun')]

#REGISTER CLASS
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    birthdate = DateField('Birthdate',[validators.DataRequired()], format='%m/%d/%Y')
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
    region = SelectField('Region', [validators.DataRequired()],choices=regions,default="",)
    #user_db = root.child
    #user_refer = db.reference('register')
    #user = U.User(name,birthdate,username,email,password)
    #user_db.push({
    #    'name': U.get_name(),
    #    'email': U.get_email(),
    #    'password': U.get_password(),
    #})

#APP ROUTE
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=["GET","POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():

        return render_template('register.html',form=form)
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

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
