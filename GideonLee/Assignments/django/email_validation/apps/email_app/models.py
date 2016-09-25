from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')

class EmailManager(models.Manager):
	# Check if valid email and create the flash message
	def validate(self, email):
		if EMAIL_REGEX.match(email):
			Email.objects.create(address=email)
			newest_email = Email.objects.filter(address=email).order_by('-address')[0]
			message = 'The email you entered(' + newest_email.address +') is a VALID email address! Thank you!'
			return ('True', message)
		else: 
			message = 'Email is not valid'
			return ('False', message) 
	# Edit the format of all of the created_at = DateTimeField(auto_now_add=True)
	def format_time(self, times):
		formatted_times = [] # Hold all of the new times
		for time in times:
			formatted_time = time[0].strftime('%m/%d/%y %I:%M%p')
			formatted_times.append(formatted_time)
		return formatted_times

class Email(models.Model):
	address = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = EmailManager()