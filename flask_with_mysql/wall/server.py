# Isaac Suntag 07/14/2017 isuntag@gmail.com

from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
import bcrypt

app = Flask(__name__)
app.secret_key = 'this_is_a_wall_key'
mysql = MySQLConnector(app, 'walldb')

# Login page
@app.route('/')
def index():
    if session and session.has_key('id'):
        return redirect('/wall')
    else:
        return render_template('index.html')
# When login form is submitted
@app.route('/login', methods=['POST'])
def login():
    # Validate entered email and password
    if len(request.form['email']) < 1 or len(request.form['password']) < 1:
        flash('Please enter your email and password.')
        return redirect('/')
    else:
        query = 'SELECT * FROM users WHERE email = :email'
        data = {
            'email': request.form['email'],
        }
        user = mysql.query_db(query, data)
        if not user or not bcrypt.checkpw(request.form['password'].encode('utf8'),user[0]['password'].encode('utf8')):
            flash('Incorrect email or password.')
            return redirect('/')
        else:
            session['id'] = user[0]['id']
            session['first_name'] = user[0]['first_name']
            return redirect('/wall')
# Registration page
@app.route('/register')
def register():
    return render_template('register.html')
#when registration form is submitted
@app.route('/create', methods=['POST'])
def create():
    # Validate if form information is valid
    valid = True
    data = {
        'first name': request.form['first_name'],
        'last name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
    }
    for key in data:
        if len(data[key]) < 1:
            flash ('Please enter ' + key)
            valid = False
    if len(data['first name']) > 0:
        if not re.match('^[A-Za-z-]', data['first name']):
            flash('First name must only contain letters or hyphen.')
            valid = False
    if len(data['last name']) > 0:
        if not re.match('^[A-Za-z-]', data['last name']):
            flash('Last name must only contain letters hypen.')
            valid = False
    if 0 < len(data['password']) < 8:
        flash('Password must be at least 8 characters long.')
        valid = False
    if not request.form['password_confirm'] == data['password']:
        flash('Passwords do not match.')
        valid = False
    if len(data['email']) > 0:
        data2 = {'email': data['email']}
        query_pw_check = 'SELECT * FROM users WHERE email = :email'
        email_check = mysql.query_db(query_pw_check, data2)
        print email_check
        if email_check:
            flash('Email already taken.')
            valid = False
        elif not re.match('[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@[A-Za-z0-9-]+(.[A-Za-z0-9]+)*(.[A-Za-z]{2,})', request.form['email']):
            flash('Incorrect email format.')
            valid = False
    if valid == True:
        hashedpw = bcrypt.hashpw(request.form['password'].encode('utf8'), bcrypt.gensalt())
        query = 'INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, NOW(), NOW())'
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashedpw,
        }
        mysql.query_db(query, data)
        query_pull = "SELECT * FROM users WHERE email = :email"
        user = mysql.query_db(query_pull, data)
        session['id'] = user[0]['id']
        session['first_name'] = user[0]['first_name']
        return redirect('/wall')
    else:
        return redirect('/register')
# The Wall Page
@app.route('/wall')
def wall():
    query_pull_posts = "SELECT messages.id, messages.message, messages.created_at, messages.updated_at, users.first_name, users.last_name FROM messages JOIN users ON messages.user_id = users.id"
    posts_pull = mysql.query_db(query_pull_posts)
    query_pull_comments = "SELECT comments.id, comments.message_id, comments.comment, comments.created_at, comments.updated_at, users.first_name, users.last_name FROM comments JOIN messages ON comments.message_id = messages.id JOIN users ON comments.user_id = users.id"
    comments_pull = mysql.query_db(query_pull_comments)
    return render_template('wall.html', posts = posts_pull, comments = comments_pull)

@app.route('/newpost', methods=['POST'])
def newpost():
    if len(request.form['post']) < 1:
        flash('Please enter a message.')
        return redirect("/wall")
    else:
        query = "INSERT INTO messages(user_id, message, created_at, updated_at) VALUES (:poster_id, :post, NOW(), NOW())"
        data = {
            'poster_id': session['id'],
            'post': request.form['post']
        }
        mysql.query_db(query, data)
        return redirect('/wall')
@app.route('/comment', methods=['POST'])
def newcomment():
    if len(request.form['comment']) < 1:
        flash('Please enter a comment.', 'commment_error')
        return redirect('/wall')
    else:
        query = "INSERT INTO comments(user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :post_id, :comment, NOW(), NOW())"
        data = {
            'user_id': session['id'],
            'post_id': request.form['post_id'],
            'comment': request.form['comment']
        }
        mysql.query_db(query, data)
        return redirect('/wall')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
