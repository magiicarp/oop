from flask import Flask, render_template, request ,flash, redirect, url_for, session
from wtforms import Form, StringField, PasswordField, TextAreaField, RadioField, SelectField, SubmitField, validators
from wtforms.fields.html5 import DateField
import firebase_admin
from firebase_admin import credentials, db
from targets2 import Target
from bmi2 import Bmi
from User import *
from datetime import datetime
from RegisterProgram import Registerform
import pygal
from pygal.style import LightSolarizedStyle


app = Flask(__name__)

cred = credentials.Certificate('./cred/oopp-267d4-firebase-adminsdk-4rnbe-fb1b31a720.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://oopp-267d4.firebaseio.com/'
})

user_ref = db.reference('userbase')
root = db.reference()
targets_ref = root.child('targets')
ref1 = db.reference()
ref2 = db.reference('BMI')

now = datetime.now()

program = db.reference('program')
registerform = db.reference('registerform')

@app.route('/')
def home():
    return render_template('index.html')


class RegisterForm(Form):
    name = StringField('Please enter your full name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('What is your Gender?', choices = [('', 'Select'), ('FEMALE', 'Female'), ('MALE', 'Male')],default='')
    email = StringField('Email', [validators.Length(min=1, max=150), validators.DataRequired()])
    contact = StringField('Contact Number', [validators.Length(min=8, max=10), validators.DataRequired()])
    weight = StringField('Weight (KG)', [validators.Length(min=1, max=150), validators.DataRequired()])
    height = StringField('Height (M)', [validators.Length(min=1, max=150), validators.DataRequired()])

@app.route('/registerprogram', methods=['GET','POST'])
def registerform():
    registerprog = RegisterForm(request.form)
    if request.method == 'POST' and registerprog.validate():
        name = registerprog.name.data
        gender = registerprog.gender.data
        email = registerprog.email.data
        contact = registerprog.contact.data
        weight = registerprog.weight.data
        height = registerprog.height.data

        registerform = Registerform(name, gender, email, contact, weight, height)

        registerform_db = root.child('registerform')
        registerform_db.push({
            'name': registerform.get_name(),
            'gender': registerform.get_gender(),
            'email': registerform.get_email(),
            'contact': registerform.get_contact(),
            'weight': registerform.get_weight(),
            'height': registerform.get_height()
        })

        flash('You have been registered for your program! Thank you!.', 'success')

    return render_template('registerform.html',registerform=registerprog)

@app.route('/fitnessprograms')
def fitnessprograms():
    return render_template('fitnessprograms.html')

class Plannerform(Form):
    age = SelectField('What is your age group?',[validators.DataRequired()], choices = [('', 'Select'), ('TEENAGER/ADULT', 'Teenager/Adult (Below 50)'), ('ELDERLY', 'Elderly (above 50)')],default='')
    type = SelectField('What type of exercise would you like to do?',[validators.DataRequired()], choices = [('', 'Select'), ('AEROBICS', 'Aerobics'), ('STRENGTH', 'Strength'), ('FLEXIBILITY', 'Flexibility')], default ='')
    time = SelectField('Choose the duration of exercise',[validators.DataRequired()], choices = [('', 'Select'), ('15min', '15 Min'), ('30min', '30 Min'), ('45min', '45 Min')], default='')


@app.route('/planner', methods=['GET','POST'])
def plannerform():
    plannerform = Plannerform(request.form)
    if request.method == 'POST' and plannerform.validate():
        age = plannerform.age.data
        type = plannerform.type.data
        time = plannerform.time.data

        routine  = ''

        if age == 'TEENAGER/ADULT':
            if type == 'AEROBICS':
                if time == '15min' :
                    routine = 'routine_1'
                elif time == '30min':
                    routine = 'routine_2'
                elif time == '45min':
                    routine = 'routine_3'

            elif type == 'STRENGTH':
                if time == '15min' :
                    routine = 'routine_4'
                elif time == '30min':
                    routine = 'routine_5'
                elif time == '45min':
                    routine = 'routine_6'

            elif type == 'FLEXIBILITY':
                if time == '15min' :
                    routine = 'routine_7'
                elif time == '30min':
                    routine = 'routine_8'
                elif time == '45min':
                    routine = 'routine_9'

        elif age == 'ELDERLY':
            if type == 'AEROBICS':
                if time == '15min':
                    routine = 'routine_10'
                elif time == '30min':
                    routine = 'routine_11'
                elif time == '45min':
                    routine = 'routine_12'

            elif type == 'STRENGTH':
                if time == '15min':
                    routine = 'routine_13'
                elif time == '30min':
                    routine = 'routine_14'
                elif time == '45min':
                    routine = 'routine_15'

            elif type == 'FLEXIBILITY':
                if time == '15min':
                    routine = 'routine_16'
                elif time == '30min':
                    routine = 'routine_17'
                elif time == '45min':
                    routine = 'routine_18'


        return redirect(url_for(routine))

    return render_template('plannerform.html',plannerform=plannerform)


@app.route('/routine_1')
def routine_1():
    return render_template('routine_1.html')

@app.route('/routine_2')
def routine_2():
    return render_template('routine_2.html')

@app.route('/routine_3')
def routine_3():
    return render_template('routine_3.html')

@app.route('/routine_4')
def routine_4():
    return render_template('routine_4.html')

@app.route('/routine_5')
def routine_5():
    return render_template('routine_5.html')

@app.route('/routine_6')
def routine_6():
    return render_template('routine_6.html')

@app.route('/routine_7')
def routine_7():
    return render_template('routine_7.html')

@app.route('/routine_8')
def routine_8():
    return render_template('routine_8.html')

@app.route('/routine_9')
def routine_9():
    return render_template('routine_9.html')

@app.route('/routine_10')
def routine_10():
    return render_template('routine_10.html')

@app.route('/routine_11')
def routine_11():
    return render_template('routine_11.html')

@app.route('/routine_12')
def routine_12():
    return render_template('routine_12.html')

@app.route('/routine_13')
def routine_13():
    return render_template('routine_13.html')

@app.route('/routine_14')
def routine_14():
    return render_template('routine_14.html')

@app.route('/routine_15')
def routine_15():
    return render_template('routine_15.html')

@app.route('/routine_16')
def routine_16():
    return render_template('routine_16.html')

@app.route('/routine_17')
def routine_17():
    return render_template('routine_17.html')

@app.route('/routine_18')
def routine_18():
    return render_template('routine_18.html')


@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/tracker')
def tracker():
    return render_template('tracker.html')


class bmiform(Form):
    weight = StringField('Weight(kg):', [validators.DataRequired()])
    height = StringField('Height(m):', [validators.DataRequired()])

@app.route('/bmi', methods=['GET','POST'])
def bmi1():
    #follow according to user profile
    #adduser = request.form[]
    #user1
    #key = session['key']
    #user = ref1.child(key)
    form = bmiform(request.form)
    if request.method =='POST' and form.validate():
        height = float(form.height.data)
        weight = float(form.weight.data)
        Bmi1 = Bmi(height, weight)
        bmi_db = ref1.child('BMI')
        #height=float(Bmi.get_height())
        #weight=float(Bmi.get_weight())
        bmi_db.push({
            "BMI":float(Bmi1.get_bmi()),
            "Date":str(now)
            })
        flash('You have successfully post your BMI','success')
        return redirect('/bmiresults')

    return render_template('bmiteseting.html', form=form)

@app.route('/bmiresults')
def bmiresults():
    bmirels = []
    bmidate = []
    ref3 = ref1.child('BMI').get()
    #bmirels = []  # create a list to store all the objects
    for ref5 in ref3:
        ref4 = ref3[ref5]
        refval = ref4['BMI']
        # retrieve date here
        refdate = ref4['Date']
        refval2 = float("{0:.2f}".format(refval))
        bmirels.append(refval2)
        bmidate.append(refdate)
    bmilast = bmirels[-1]
    graph = pygal.Line(style=LightSolarizedStyle)
    graph.title = 'BMI history'
    graph.x_labels = bmidate
    #graph.y_labels = ['11','13','15','17','19','21','23','25','27','29','31']
    graph.add('BMI', bmirels)
    graph_data = graph.render_data_uri()
    return render_template('bmiresults.html' , bmilist2=bmirels, bmilast=bmilast, graph_data= graph_data)

root = db.reference()
#targets_ref = root.child('targets')

@app.route('/viewtarget')
def viewtarget():
    #print(root.get())
    targets = root.child('targets').get()
    list1 = []  # create a list to store all the objects
    for target6 in targets:
        targetpost = targets[target6]
        target2 = Target(targetpost['goals'], targetpost['category'], targetpost['status'], targetpost['number'])
        target2.set_target3(target6)
        target2.get_target3()
        list1.append(target2)
        #return render_template('view_target.html', targets=list1)

    return render_template('view_target.html', targets=list1)

class RequiredIf(object):

    def __init__(self, *args, **kwargs):
        self.conditions = kwargs

    def __call__(self, form, field):
        for name, data in self.conditions.items():
            if name not in form._fields:
                validators.Optional()(field)
            else:
                condition_field = form._fields.get(name)
                if condition_field.data == data:
                    validators.DataRequired().__call__(form, field)
                else:
                    validators.Optional().__call__(form, field)

class Target1(Form):
    goals = StringField('Goals', [validators.Length(min=1, max=150), validators.DataRequired()])
    category = RadioField('Type Of Goals', choices=[('physical', 'Physical'), ('diet', 'Diet'), ('habits', 'Habits')])
    status = RadioField('Status', choices=[('active', 'Active'),('onhold', 'On Hold'), ('notstarted', 'Not Started'), ('completed', 'Completed')])
    number = StringField('Number of times daily',[validators.Length(min=1, max=100), validators.DataRequired()])
    submit = SubmitField('Update')

@app.route('/newtarget', methods=['GET','POST'])
def new():
    targetform = Target1(request.form)
    if request.method == 'POST' and targetform.validate():
        goals = targetform.goals.data
        category = targetform.category.data
        status = targetform.status.data
        number = targetform.number.data
        tar = Target(goals, category, status, number)
        tar_db = root.child('targets')
        tar_db.push({
            'goals': tar.get_goals(),
            'category': tar.get_category(),
            'status': tar.get_status(),
            'number': tar.get_number(),
        })
        flash('Target added.', 'success')
        return redirect(url_for('viewtarget'))

    return render_template('create_target.html', form=targetform)

@app.route('/update/<string:id>', methods=['GET','POST'])
def update_target(id):
    targetform = Target1(request.form)
    if request.method == 'POST' and targetform.validate():
        goals = targetform.goals.data
        category = targetform.category.data
        status = targetform.status.data
        number = targetform.number.data
        tar = Target(goals, category, status, number)
        tar_db = root.child('targets/' + id)
        tar_db.set({
            'goals': tar.get_goals(),
            'category': tar.get_category(),
            'status': tar.get_status(),
            'number': tar.get_number(),
        })
        flash('Goals Updated Successfully.', 'success')
        return redirect(url_for('viewtarget'))
    else:
        url = 'targets/' + id
        target_s = root.child(url).get()
        target2 = Target(target_s['goals'], target_s['category'], target_s['status'], target_s['number'])
        target2.set_target3(id)
        targetform.goals.data = target2.get_goals()
        targetform.category.data = target2.get_category()
        targetform.status.data = target2.get_status()
        targetform.number.data = target2.get_number()

        return render_template('update_target.html', form=targetform)

    #return render_template('update_target.html', form=targetform)

@app.route('/delete_targets/<string:id>', methods=['POST'])
def delete_targets(id):
    tar_db = root.child('targets/' + id)
    tar_db.delete()
    flash('Deleted', 'success')

    return redirect(url_for('viewtarget'))

@app.route('/foodtracker' , methods=['GET','POST'])
def food():
    ref = db.reference('')
    for i in ref:
        count += 0
        foodtracker_db = root.child('report/end/foods/'+ count + '/nutrients/0/value')
        foodtracker_db = root.child('report/end/foods/0/nutrients/0/value')
    cal1 = ref.order_by_child('foodtracker/report/end/foods')
    cal2 = ref.order_by_child('foodtracker/report/end/foods/0/nutrients/0/value').get()
    #calories = {'Boiled Eggs': 155, 'Fried Eggs': 196, 'Whole Chicken': 1070, 'French Fries': 312,'Celery': 16, 'Broccoli': 34, 'Cabbage': 25, 'Potato': 77, 'Apple': 52, 'Cucumber': 16,
     #           'Onion':40,'White Rice(132g, a cup)': 199, 'Chicken': 239, 'Beef': 250}
    list2 = []
    list3 = []
    #foas = ref.get()
    for cals in cal1:
        list2.append(cals)
    for cals2 in cal2:
        list3.append(cals2)
        return render_template('foodtracker.html', calories=list2, cal2=list3)

   #     else:
             #display results
   #         return render_template('foodtracker.html', search1=list1, search2=list2)
    #count = 0
    #for i in calories:
     #   count += 1
    #if click == True:
     #   sum(calories.values())
    #return render_template('foodtracker.html', calories=list1, cal2=list2)

__all__ = ['Target' , 'Bmi' , 'Food']


#profile
@app.route('/<username>')
def profile(username):
    return render_template('profile.html')

#class ProfileForm(Form):
    #about = TextAreaField('About')

@app.route('/<username>/edit')
def editprofile(username):
    if session['logged_in'] == True:
        return render_template('editprofile.html')
        #form = ProfileForm(request.form)
        #if request.method == 'POST' and form.validate():
        #    about = form.about.data
        #user_db = root.child('userbase')
        #user_db.push({
        #    'about': about
        #})
    else:
        flash('You need to be logged in to edit your profile.')



#signup
class SignUpForm(Form):
    name = StringField('Name', [validators.Length(min=1, max =50), validators.DataRequired()])
    username = StringField('Username',[validators.Length(min=4,max=25),validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=6,max=50),validators.DataRequired()])
    birthday = DateField('Birthday', format='%Y-%m-%d')
    #gender = SelectField('Gender',choices=['Female', 'Male', 'Other'])
    password = PasswordField('Password', [validators.DataRequired(),validators.EqualTo('confirm',message='Passwords do not match')
])
    confirm = PasswordField('Confirm Password')

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data.title()
        username = form.username.data
        email = form.email.data
        birthday = str(form.birthday.data)
        #gender = form.gender.data
        password = str(form.password.data)
        userbase = user_ref.get()
        user_db = root.child('userbase')
        user = User(name, username, email,birthday, password)
        user_db.push({
            'name': user.get_name(),
            'username': user.get_username(),
            'email': user.get_email(),
            'birthday': user.get_birthday(),
            #'gender': user.get_gender(),
            'password': user.get_password()
        })
        flash('You have registered successfully', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

#login
class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

@app.route('/login', methods=['GET', 'POST'])
def login():
     form = LoginForm(request.form)
     if request.method == 'POST' and form.validate() == True:
         username = form.username.data
         password = form.password.data
         userbase = user_ref.get()
         for user in userbase.items():
             if user[1]['username'] == username and user[1]['password'] == password:
                 session['user_data'] = user[1]
                 session['logged_in'] = True
                 session['username'] = username
                 return redirect(url_for('home'))
             elif form.validate() == False:
                 flash('Please enter your credentials', 'danger')
                 return render_template('login.html', form=form)
             else:
                 flash('Wrong credentials. Please try again', 'danger')
                 return render_template('login.html', form=form)
     return render_template('login.html', form=form)


#logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

#requiredif
class RequiredIf(object):

    def __init__(self, *args, **kwargs):
        self.conditions = kwargs

    def __call__(self, form, field):
        for name, data in self.conditions.items():
            if name not in form._fields:
                validators.Optional()(field)
            else:
                condition_field = form._fields.get(name)
                if condition_field.data == data:
                    validators.DataRequired().__call__(form, field)
                else:
                    validators.Optional().__call__(form, field)



if __name__ == '__main__':
    app.secret_key = 'secret12'
    app.run(port=80,debug= True)
