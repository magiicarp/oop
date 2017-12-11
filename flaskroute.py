from flask import Flask, render_template


app = Flask(__name__)

@app.route('/home')
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

if __name__ == '__main__':
    app.run()
