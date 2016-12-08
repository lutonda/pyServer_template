from flask import Flask, render_template, json, request

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'local_user_1'
app.config['MYSQL_DATABASE_PASSWORD'] = '9e2244'
app.config['MYSQL_DATABASE_DB'] = 'local_lab_1'
app.config['MYSQL_DATABASE_HOST'] = 'db4free.net'
mysql.init_app(app)
