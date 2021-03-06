from flask import Flask, render_template, request, redirect, flash, session
from flask_bcrypt import Bcrypt
from connection import MySQLConnector
import re

# CONSTANTS
app = Flask(__name__)
db = MySQLConnector(app, 'TheWall')
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
app.secret_key = 'keepitsecretkeepitsafe'
bcrypt = Bcrypt(app)

# SQL QUERIES
queries = {
	'create' :'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())',
	'get_by_id' : 'SELECT first_name, last_name, email FROM users WHERE id = :id',
	'get_by_email' : 'SELECT id, password FROM users WHERE email = :email',
	'post_message' : 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())',
	'post_comment' : 'INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW())',
	'get_messages' : 'SELECT * FROM messages',
	'get_comments' : 'SELECT * FROM comments',
	'get_users' : 'SELECT * FROM users',
}


# ROUTING
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	potential_errors = validate_login(request.form)
	if len(potential_errors[0]) > 0:
		print_flash_messages(potential_errors)
		return redirect('/')
	return login_user_by_id(potential_errors[1])

@app.route('/register', methods=['POST'])
def register():
	potential_errors = validate_registration(request.form)
	if len(potential_errors) > 0:
		print_flash_messages(potential_errors)
		return redirect('/')
	password = bcrypt.generate_password_hash(request.form['password'])
	query = queries['create']
	data = {
		'first_name' : request.form['first_name'],
		'last_name' : request.form['last_name'],
		'email' : request.form['email'],
		'password' : password
	}
	new_user_id = db.query_db(query, data)
	return login_user_by_id(new_user_id)

@app.route('/wall')
def wall():
	query = queries['get_messages']
	data = {}
	messages = db.query_db(query, data)
	query = queries['get_comments']
	data = {}
	comments = db.query_db(query, data)
	query = queries['get_users']
	data = {}
	users = db.query_db(query, data)
	return render_template('wall.html', messages = messages, comments = comments, users = users)

@app.route('/logout')
def logout():
	session.pop('user')
	return redirect('/')

@app.route('/message', methods=['POST'])
def message():
	query = queries['post_message']
	data = {
		'user_id' : session['id'],
		'message' : request.form['message']	
	}
	new_message = db.query_db(query, data)
	return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
	query = queries['post_comment']
	data = {
		'message_id' : request.form['message_id'],
		'user_id' : session['id'],
		'comment' : request.form['comment'],
	}
	new_comment = db.query_db(query, data)
	return redirect('/wall')



# HELPER FUNCTIONS
def validate_registration(form_info):
	errors = []
	if len(form_info['first_name']) < 2 or len(form_info['last_name']) < 2:
		errors.append("First/Last name must be at least 2 characters.")
	if not (EMAIL_REGEX.match(form_info['email'])) or len(form_info['email']) < 1:
		errors.append("Must be a valid email")
	if len(form_info['password'])<8 or form_info['password'] != form_info['password_confirm']:
		errors.append("Passwords must match and not be blank")
	return errors

def validate_login(form_info):
	errors = []
	query = queries['get_by_email']
	data = {
	'email' : form_info['email']
	}
	potential_user = db.query_db(query, data)
	if len(potential_user) < 1:
		errors.append("email not in system")
		return (errors, None)
	if not bcrypt.check_password_hash(potential_user[0]['password'], form_info['password']):
		print potential_user[0]['id']
		errors.append("Email/password don't match")
		return (errors, None)

	return (errors, potential_user[0]['id'])

def print_flash_messages(message_list):
	for message in message_list:
		flash(message)

def login_user_by_id(id):
	query = queries['get_by_id']
	data = {
		'id': id
	}
	user = db.query_db(query, data)[0]
	session['id'] = id
	session['user'] = user
	return redirect('/wall')

app.run(debug=True)