from os import error
from flask import Flask, request, render_template
from autoScreening import autoScreening

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == '' or password == '':
            return render_template('error.html', error="Enter the username and password")

        try:
            autoScreening(username, password)
            return render_template('success.html')
        except:
            return render_template('error.html', error="An error occured, maybe your login details have an error")
    else:
        return render_template('login_sfsu.html')

app.run(debug=False, host="0.0.0.0")