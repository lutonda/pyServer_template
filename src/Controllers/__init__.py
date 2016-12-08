from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL
#from flask_mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

@app.route('/')
def maini():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html', entries=['a', 'b', 'c', 'd', 'e'])


@app.route('/ola')
def main(app):
    return render_template('index.html')