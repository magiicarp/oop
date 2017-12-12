from flask import Flask, render_template, request ,flash, redirect, url_for


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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

@app.route('/tracker')
def tracker():
    return render_template('tracker.html')

@app.route('/teenagerplan')
def teenagerplan():
    return render_template('teenagerplan.html')

@app.route('/teenageraerobics')
def teenageraerobics():
    return render_template('teenageraerobics.html')

@app.route('/teenageraerobic30min')
def teenageraerobic30min():
    return render_template('teenageraerobic30min.html')

if __name__ == '__main__':
    app.run()
