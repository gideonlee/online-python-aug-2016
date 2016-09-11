from flask import Flask, render_template, redirect, request, jsonify
from sqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'ajax_posts_db')

queries = {
	'show_all': 'SELECT * FROM posts',
	'create': 'INSERT INTO posts(description, created_at, updated_at) VALUES(:note, NOW(), NOW())',
	'show_new': 'SELECT * FROM posts WHERE description=:note ORDER BY id DESC LIMIT 1'
}

@app.route('/')
def reroute():
	return redirect('/posts')

@app.route('/posts')
def index():
	notes = mysql.query_db(queries['show_all'])
	return render_template('index.html', notes=notes)

@app.route('/posts/create', methods=['POST'])
def create():
	data = {
		'note': request.form['note']
	}
	mysql.query_db(queries['create'] ,data)
	
	new_note = mysql.query_db(queries['show_new'], data)
	# new_note is a list with one object inside [{}]
	# [ {
	# 	'id':
	# 	'description':
	# 	'updated_at':
	# 	'created_at':
	# } ]
	
	return jsonify(new_note=new_note)
	# Jsonify turns my newly created list(object) into object with an object which contains a list {{[]}}:
	# { { [ 
	#  'id' 
	#  'description'
	#  'created_at'
	#  'updated_at'
	# ] } }

if __name__ == '__main__':
	app.run(debug=True)