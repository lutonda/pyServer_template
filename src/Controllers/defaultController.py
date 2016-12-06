from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL
from app import app
from werkzeug import generate_password_hash, check_password_hash
#from src._conf.server import start
mysql = MySQL()
#app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html', entries=['a', 'b', 'c', 'd', 'e'])


@app.route('/ola')
def maini(app):
    return render_template('index.html')

@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:

            print('message User created successfully !')
            return json.dumps({'message': 'User created successfully !'})
            # All Good, let's call MySQL

            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser', (_name, _email, _hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message': 'User created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()