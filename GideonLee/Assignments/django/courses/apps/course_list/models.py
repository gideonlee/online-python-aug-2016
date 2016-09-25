from __future__ import unicode_literals
from django.db import models
import random 
import re

# Create a list of links to append new images, loop through this list
# Create a delete page
SYMBOLS = re.compile(r'^[\W]+')
images = ['course_list/images/art.jpg', 'course_list/images/business.jpg', 'course_list/images/dog.jpg', 'course_list/images/fingers.jpg', 'course_list/images/glasses.jpg', 'course_list/images/house.jpg', 'course_list/images/marine.jpg', 'course_list/images/money.jpg', 'course_list/images/oil.jpg', 'course_list/images/rainbow.jpg', 'course_list/images/yoga.jpg']

class CourseManager(models.Manager):
	def validate(self, **kwargs):
		errors = []
		picture = random.choice(images)
		if SYMBOLS.match(kwargs['name']):
			errors.append('Course Name cannot start with these symbols ".-+_@$%^&*".')
		if len(kwargs['name']) < 1:
			errors.append('Course Name cannot be empty.')
		if len(kwargs['description']) < 1: 
			errors.append('Course description cannot be empty.')	
		if errors: 
			return (False, errors)
		else: 
			new_course = Course.objects.create(name=kwargs['name'], description=kwargs['description'], photo=picture)
			course = Course.objects.get(name=kwargs['name'])
			return (True, course)

class Course(models.Model):
	name = models.CharField(max_length=45)
	description = models.TextField(max_length=1000)
	photo = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = CourseManager()

class Comment(models.Model):
	comments = models.TextField(max_length=1000)
	course = models.ForeignKey(Course)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

