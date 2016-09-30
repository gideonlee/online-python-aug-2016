from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User, UserManager, Author, Book, BookManager, Review
from django.contrib import messages

# Create your views here.
def index(request):
	# Author.objects.all().delete()
	# Book.objects.all().delete()
	# Review.objects.all().delete()
	return render(request, 'book_reviews/index.html')

def home(request):
	if 'user_id' in request.session:
		user = User.objects.get(id=request.session['user_id'])
		books = Book.objects.all()
		recent_reviews = Review.objects.all().order_by('-id')[:3]
		context = {
			'name': user.name.title(),
			'alias': user.alias,
			'emai': user.email,
			'books': books,
			'recent_reviews': recent_reviews,
		}
		return render(request, 'book_reviews/home.html', context)
	return redirect(reverse('book_reviews/index'))

def register(request):
	if request.method == 'POST':
		result = User.objects.validate_new(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=request.POST['password'], confirm_password=request.POST['confirm_password'])
		if result[0]:
			request.session['user_id'] = result[1]
			return redirect(reverse('book_reviews:home'))
		else:
			for error in result[1]:
				messages.error(request, error)
			return redirect(reverse('book_reviews:index'))

def login(request):
	if request.method == 'POST':
		result = User.objects.validate_login(email=request.POST['email'], password=request.POST['password'])
		if result[0]:
			request.session['user_id'] = result[1]
			return redirect(reverse('book_reviews:home'))
		else: 
			for error in result[1]:
				messages.error(request, error)
			return redirect(reverse('book_reviews/index'))

def logout(request):
	request.session.pop('user_id')
	return redirect(reverse('book_reviews:index'))

def add(request):
	return render(request, 'book_reviews/add.html')

def process(request):
	book_id = new_book_and_review = Book.objects.add_book_review(user_id=request.session['user_id'], title=request.POST['title'], author=request.POST['author'], preset_author=request.POST['preset_author'], stars=request.POST['stars'], review=request.POST['review'])
	return redirect(reverse('book_reviews:show_book', kwargs={'id': book_id}))

def show_book(request, id):
	book = Book.objects.get(id=id)
	author = book.author
	reviews = Review.objects.filter(book=book)
	context = {
		'book': book,
		'reviews': reviews,
	}
	return render(request,'book_reviews/show.html', context)

def show_user(request, id):
	info = User.objects.profile_info(id=id)
	context = {
		'user': info[0],
		'reviews': info[1],
		'total_reviews': info[2],
	}
	return render(request, 'book_reviews/profile.html', context)

def destroy(request, id):
	# Review.objects.get(id=id).delete()
	Review.objects.destroy_review(review_id=id, book_id=request.POST['book_id'])
	return redirect(reverse('book_reviews:show_book', kwargs={'id': request.POST['book_id']}))