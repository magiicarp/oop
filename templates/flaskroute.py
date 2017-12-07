from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField

import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('C:/Users/Aaron Lam/PycharmProjects/LibrarySystem')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'database url where you noted down in 5.1 Create Firebase Account '
})

root = db.reference()

app = Flask(__name__)

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()



@app.route('/home')
def home():
    return render_template('index.html')



