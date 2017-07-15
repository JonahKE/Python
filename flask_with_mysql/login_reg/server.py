from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
import bcrypt

app = Flask(__name__)
app.secret_key = 'key'
mysql = MySQLConnector(app, 'loginregdb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
    if len(request.form['email']) < 1 or len(request.form['password']) < 1:
        flash('Please enter your email and password.')
        return redirect('/')
    else:
        query = 'SELECT * FROM users WHERE email = :email'
        data = {
            'email': request.form['email'],
        }
        valid = mysql.query_db(query, data)
        if not valid or not bcrypt.checkpw(request.form['password'].encode('utf8'),valid[0]['password'].encode('utf8')):
            flash('Incorrect email or password')
            return redirect('/')
        else:
            session['user_data'] = valid
            return redirect('/loggedin')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/adduser', methods=['POST'])
def add():
    query = 'SELECT * FROM users WHERE email = :email'
    data = {
        'email': request.form['email']
    }
    email_check = mysql.query_db(query, data)
    valid = True
    if email_check:
        flash('Email already taken.')
        valid = False
    if len(request.form['first_name']) < 2:
        flash('Please enter your first name. It must be at least two letters long.')
        valid = False
    elif not re.match(r'[a-zA-Z]', request.form['first_name']):
        flash('Your first name may only contain letters.')
        valid = False
    if len(request.form['last_name']) < 2:
        flash('Please enter your last name. It must be at least two letters long.')
        valid = False
    elif not re.match(r'[a-zA-Z]', request.form['last_name']):
        flash('Your last name may only contain letters.')
        valid = False
    if len(request.form['email']) < 1:
        flash('Please enter your email.')
        valid = False
    if len(request.form['password']) < 1:
        flash('Please enter a password.')
        valid = False
    elif len(request.form['password']) < 8:
        flash('Password much be at least 8 characters long.')
        valid = False
    elif request.form['password'] != request.form['password_confirm']:
        flash('Passwords do not match.')
        valid = False

    if valid == False:
        return redirect('/register')
    else:
        hashedpw = bcrypt.hashpw(':password', bcrypt.gensalt())
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'
        hashedpw = bcrypt.hashpw(request.form['password'].encode('utf8'), bcrypt.gensalt())
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashedpw
        }
        mysql.query_db(query, data)
        query = 'SELECT * FROM users WHERE email = :email'
        session['user_data'] = mysql.query_db(query, data)
        return redirect('/loggedin')

@app.route('/loggedin')
def loggedin():
    return render_template('loggedin.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
