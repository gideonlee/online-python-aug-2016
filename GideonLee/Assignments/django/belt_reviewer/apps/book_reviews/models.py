from __future__ import unicode_literals
from django.db import models
import bcrypt
import re 
from django.db.models import Count

EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')

class UserManager(models.Manager):
	def validate_new(self, **kwargs):
		errors = []

		if len(kwargs['name']) < 2:
			errors.append('Name must be longer than 2 characters.')
		if not EMAIL_REGEX.match(kwargs['email']): 
			errors.append('Not a valid email.')
		email_exists = User.objects.filter(email=kwargs['email'])
		if email_exists:
			errors.append('Email already registered.')
		if len(kwargs['password']) < 8:
			errors.append('Password must be at least 8 characters long.')
		if kwargs['password'] != kwargs['confirm_password']:
			errors.append('Passwords do not match.')

		if errors: 
			return (False, errors)
		else: 
			input_pw = kwargs['password'].encode()
			hashed_pw = bcrypt.hashpw(input_pw, bcrypt.gensalt())
			User.objects.create(name=kwargs['name'], alias=kwargs['alias'], email=kwargs['email'], password=hashed_pw)
			user = User.objects.get(name=kwargs['name'], alias=kwargs['alias'], email=kwargs['email'], password=hashed_pw)
			return (True, user.id)
	def validate_login(self, **kwargs):
		errors = []
		try:
			user = User.objects.get(email__iexact=kwargs['email'])
			return (True, user.id)
		except:
			errors.append('Invalid Email/Password')
			return (False, errors)
	def profile_info(self, **kwargs):
		user = User.objects.get(id=kwargs['id'])
		reviews = Review.objects.filter(user=user)
		total_reviews = len(reviews)
		return (user, reviews, total_reviews)

class BookManager(models.Manager):
	def add_book_review(self, **kwargs):
		if kwargs['author'] == '':
			author_name = kwargs['preset_author']
		else:
			author_name = kwargs['author']

		try: 
			author = Author.objects.get(name=author_name)
		except:
			author = Author.objects.create(name=author_name)
		try: 
			book = Book.objects.get(title=kwargs['title'])
		except: 
			book = Book.objects.create(title=kwargs['title'], author=author)

		user = User.objects.get(id=kwargs['user_id'])
		Review.objects.create(description=kwargs['review'], book=book, user=user, stars=kwargs['stars'])
		return book.id

class ReviewManager(models.Manager):
	def destroy_review(self, **kwargs):
		Review.objects.get(id=kwargs['review_id']).delete()

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Author(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(Author)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = BookManager()

class Review(models.Model):
	description = models.TextField(max_length=1000)
	book = models.ForeignKey(Book)
	user = models.ForeignKey(User)
	stars = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ReviewManager()
