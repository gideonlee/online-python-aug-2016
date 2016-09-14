from flask import Flask, render_template, request, redirect, jsonify
from sqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'ajax_notes_db')

queries = {
	'show_all': 'SELECT * FROM notes',
	'create': 'INSERT INTO notes(title, created_at, updated_at) VALUES(:new_title, NOW(), NOW())',
	'delete': 'DELETE FROM notes WHERE id=:id',
	'add_description': 'UPDATE notes SET description=:description WHERE id=:id'
}

@app.route('/')
def reroute():
	return redirect('/notes')

@app.route('/notes', methods=['get'])
def index():
	notes = mysql.query_db(queries['show_all'])
	return render_template('index.html', notes=notes)

@app.route('/notes/create', methods=['post'])
def create():
	data = {
		'new_title': request.form['new_title']
	}
	mysql.query_db(queries['create'], data)
	return redirect('/get_all_notes')
	# notes = mysql.query_db(queries['show_all'])
	# return render_template('/partials/notes.html', notes=notes)

@app.route('/notes/<id>/delete', methods=['post'])
def delete(id):
	data = {
		'id': id
	}
	mysql.query_db(queries['delete'], data)
	return redirect('/get_all_notes')
	# notes = mysql.query_db(queries['show_all'])
	# return render_template('/partials/notes.html', notes=notes)

@app.route('/notes/<id>/description', methods=['post'])
def description(id):
	data = {
		'id': id,
		'description': request.form['description']
	}
	mysql.query_db(queries['add_description'], data)
	return redirect('/get_all_notes')
	# notes = mysql.query_db(queries['show_all'])
	# return render_template('/partials/notes.html', notes=notes)

# This will get rid of the repeat code that I've commented out. 
@app.route('/get_all_notes')
def all_notes():
	notes = mysql.query_db(queries['show_all'])
	return render_template('/partials/notes.html', notes=notes)

if __name__ == '__main__':
	app.run(debug=True)
