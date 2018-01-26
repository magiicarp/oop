from flask import Flask, render_template, request ,flash, redirect, url_for
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, SubmitField, validators
from target1 import Target
import firebase_admin
from firebase_admin import credentials, db
from target1 import Target
#from bmi1 import Bmi
from User import User

app = Flask(__name__)

cred = credentials.Certificate('./cred/targets-settings-firebase-adminsdk-04p4y-fa9131dc22.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://targets-settings.firebaseio.com/'
})

root = db.reference()
targets_ref = root.child('targets')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/healthyeating')
def healthyeating():
    return render_template('eating.html')


class Plannerform(Form):
    age = SelectField('What is your age group?', choices = [('', 'Select'), ('TEENAGER', 'Teenager (13-19 Years)'), ('ADULT', 'Adult (20-49 Years)'), ('ELDERLY', 'Elderly (above 50)')],default='')
    type = SelectField('What type of exercise would you like to do?', choices = [('', 'Select'), ('AEROBICS', 'Aerobics'), ('STRENGTH', 'Strength'), ('FLEXIBILITY', 'Flexibility')], default ='')
    time = SelectField('Choose the duration of exercise', choices = [('', 'Select'), ('30min', '30 Min'), ('60min', '60 Min'), ('90min', '90 Min')], default='')

@app.route('/planner', methods=['GET','POST'])
def plannerform():
    plannerform = Plannerform(request.form)
    if request.method == 'POST' and plannerform.validate():
        age = plannerform.age.data
        type = plannerform.type.data
        time = plannerform.time.data

        routine  = ''

        if age == 'TEENAGER':
            if type == 'AEROBICS':
                if time == '30min' :
                    routine = 'routine_1'
                elif time == '60min':
                    routine = 'routine_2'
                elif time == '90min':
                    routine = 'routine_3'

            elif type == 'STRENGTH':
                if time == '30min' :
                    routine = 'routine_4'
                elif time == '60min':
                    routine = 'routine_5'
                elif time == '90min':
                    routine = 'routine_6'

            elif type == 'FLEXIBILITY':
                if time == '30min' :
                    routine = 'routine_7'
                elif time == '60min':
                    routine = 'routine_8'
                elif time == '90min':
                    routine = 'routine_9'

        elif age == 'ADULT':
            if type == 'AEROBICS':
                if time == '30min':
                    routine = 'routine_10'
                elif time == '60min':
                    routine = 'routine_11'
                elif time == '90min':
                    routine = 'routine_12'

            elif type == 'STRENGTH':
                if time == '30min':
                    routine = 'routine_13'
                elif time == '60min':
                    routine = 'routine_14'
                elif time == '90min':
                    routine = 'routine_15'

            elif type == 'FLEXIBILITY':
                if time == '30min':
                    routine = 'routine_16'
                elif time == '60min':
                    routine = 'routine_17'
                elif time == '90min':
                    routine = 'routine_18'

        elif age == 'ELDERLY':
            if type == 'AEROBICS':
                if time == '30min':
                    routine = 'routine_19'
                elif time == '60min':
                    routine = 'routine_20'
                elif time == '90min':
                    routine = 'routine_21'

            elif type == 'STRENGTH':
                if time == '30min':
                    routine = 'routine_22'
                elif time == '60min':
                    routine = 'routine_23'
                elif time == '90min':
                    routine = 'routine_24'

            elif type == 'FLEXIBILITY':
                if time == '30min':
                    routine = 'routine_25'
                elif time == '60min':
                    routine = 'routine_26'
                elif time == '90min':
                    routine = 'routine_27'

        return redirect(url_for(routine))

    return render_template('plannerform.html',plannerform=plannerform)


@app.route('/routine_1')
def routine_1():
    return render_template('routine_1.html')

@app.route('/routine_2')
def routine_2():
    return render_template('routine_2.html')


@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/tracker')
def tracker():
    return render_template('tracker.html')

@app.route('/teenagerplan')
def teenagerplan():
    return render_template('teenagerplan.html')


@app.route('/bmi', methods=['GET','POST'])
class bmi(Form):
    weight = StringField('Weight:', [validators.DataRequired()])
    height = StringField('Height:', [validators.DataRequired()])

def calculate():
    #follow according to user profile
    #adduser = request.form[]
    #user1
    form = bmi(request.form)
    if request.method == 'POST' and form.validate():
        weight = float(form.weight.data)
        height = float(form.height.data)
        Bmi = bmi1.Bmi(height, weight)
        bmi_db = User.child('BMI')
        bmi_db.update({
            "height":float(Bmi.get_height()),
            "weight":float(Bmi.get_weight()),
            "BMI":str(Bmi.get_bmi())
        })
        flash('You have successfully post your BMI','success')
        return redirect(url_for('bmi'))
    return render_template('bmiteseting.html')
@app.route('/viewtarget')
def viewtarget():
    #print(root.get())
    list1 = []  # create a list to store all the objects
    targets = targets_ref.get()
    for target3 in targets:
        targetpost = targets[target3]
        target2 = Target1(targetpost['goals'], targetpost['category'], targetpost['status'], targetpost['number'])
        target2.set_target3(target3)
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
        tar = Target1(goals, category, status, number)
        tar_db = root.child('targets')
        tar_db.push({
            'goals': tar.get_goals(),
            'category': tar.get_category(),
            'status': tar.get_status(),
            'number': tar.get_number(),
  #          'start_date': tar.get_start_date(),
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
        tar = Target1(goals, category, status, number)
        tar_db = root.child('targets/' + id)
        tar_db.set({
            'goals': tar.get_goals(),
            'category': tar.get_category(),
            'status': tar.get_status(),
            'number': tar.get_number(),
        #          'start_date': tar.get_start_date(),
        })
        flash('Goals Updated Successfully.', 'success')
        return redirect(url_for('viewtarget'))
    else:
        url = 'targets/' + id
        target_s = root.child(url).get()

        target2 = Target1(target_s['goals'], target_s['category'], target_s['status'], target_s['number'])
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


@app.route('/foodtracker')
def food():
    calories = {'Boiled Eggs': 155, 'Fried Eggs': 196, 'Whole Chicken': 1070, 'French Fries': 312,'Celery': 16, 'Broccoli': 34, 'Cabbage': 25, 'Potato': 77, 'Apple': 52, 'Cucumber': 16,
                'Onion':40,'White Rice(132g, a cup)': 199, 'Chicken': 239, 'Beef': 250}

    count = 0
    for i in calories:
        count += 1
    #if click == True:
        sum(calories.values())
    return render_template('foodtracker.html', calories=calories)


if __name__ == '__main__':
    app.secret_key = 'secret12'
    app.run(port=80) 
