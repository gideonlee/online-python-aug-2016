from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')

class UserManager(models.Manager):
	def validate(self, **kwargs):
		errors = []
		# Names must be valid 
		if not kwargs['first_name'].isalpha() or len(kwargs['first_name']) < 2:
			errors.append('First Name must be at least 2 characters and contain no numbers.')
		if not kwargs['last_name'].isalpha() or len(kwargs['last_name']) < 2: 
			errors.append('Last Name must be at least 2 characters and contain no numbers.')
		# Email must be valid 
		if not EMAIL_REGEX.match(kwargs['email']):
			errors.append('This is not a valid email.')

		# Birthday must be valid 
		now = datetime.now()
		this_year = int(now.strftime('%Y'))
		if len(kwargs['dob']) < 1:
			errors.append('Birthday cannot be empty.')		
		else: 
			their_birth_year = int(kwargs['dob'][-4:])
			if this_year - their_birth_year < 18: 
				errors.append('You must be 18 or older to attend.')
			else:
				dob = kwargs['dob'][-4:]+'-'+kwargs['dob'][:2]+'-'+kwargs['dob'][3:5]

		# Password must be valid
		if len(kwargs['password']) < 8:
			errors.append('Password must be at least 8 characters long.')
		if kwargs['password'] != kwargs['confirm_password']:
			errors.append('Passwords do not match.')	

		if errors: 
			# Return false and send the errors list
			return (False, errors)
		else: 
			# Encode the password and push this user into the db
			encoded = kwargs['password'].encode()
			hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

			# Create the new user and use the get method to return this new user's id
			User.objects.create(first_name=kwargs['first_name'], last_name=kwargs['last_name'], dob=dob, email=kwargs['email'], password=hashed)
			user = User.objects.get(first_name=kwargs['first_name'], last_name=kwargs['last_name'], dob=dob, email=kwargs['email'])
			user_id = str(user.id)
			return (True, user_id)

	def login(self, **kwargs):
		errors = []
		# Use try because if User.objects.get doesn't return anything it'll be an error. 
		# One other alternative possible solution is to use .filter and see if the result returns back an empty querySet. 
		try:
			user = User.objects.get(email__iexact=kwargs['email'])

			# Must encode both hashed db password and input password before passing into bcrypt
			hashed_pw = user.password.encode() 
			input_pw = kwargs['password'].encode() 
			
			# Pass the user input and hashed db password and check it: 
			if bcrypt.hashpw(input_pw, hashed_pw) == hashed_pw:
				user_id = str(user.id)
				return (True, user_id)
			else:
				errors.append('Invalid user/password.')	
				return (False, errors)
		except: 
			print 'if user is correct, will it still go in here?'
			errors.append('Invalid user/password.')	
			return (False, errors)

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	dob = models.DateField()
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
