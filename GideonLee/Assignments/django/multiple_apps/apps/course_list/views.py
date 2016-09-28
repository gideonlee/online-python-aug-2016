from django.shortcuts import render, redirect
from .models import CourseManager, Course, Comment, User
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Count

# Show all the Courses
def index(request):
	courses = Course.objects.all()
	context = {
		'courses': courses 
	}
	return render(request, 'course_list/index.html', context)

# Pushes the courses into a validate Manager function created in models.py
def add_course(request):
	new_course = Course.objects.validate(name=request.POST['name'], description=request.POST['description'])
	
	# Produce an error in the terminal. Maybe get it display on the front page?
	if not new_course[0]: 
		for message in new_course[1]:
			messages.error(request, message)
	return redirect(reverse('course_list:index'))

# Sends user to a confirm delete page which will allow them to confirm to delete
def confirm_delete(request, id):
	course_to_delete = Course.objects.get(id=id)
	context = {
		'course': course_to_delete
	}
	return render(request, 'course_list/confirm_delete.html', context)

# Deletes the course from the django db 
def delete(request):
	delete_course = Course.objects.get(id=request.POST['course_id']).delete()
	return redirect(reverse('course_list:index'))

# Goes to a comments page to display all the comments
def comments(request, id):
	course = Course.objects.get(id=id)
	# comments = Comment.objects.all().delete()
	comments = Comment.objects.filter(course__id=id)
	context = {
		'course': course,
		'comments': comments
	}
	return render(request, 'course_list/comments.html', context)

# Allows the user to post a comment about the course
def post_comment(request, id):
	course = Course.objects.get(id=id)
	Comment.objects.create(comments=request.POST['comment'], course=course)
	return redirect(reverse('course_list:comments', kwargs={'id':id}))
	# return redirect('/comments/'+id)

# Allows the user to delete a comment about the course 
def delete_comment(request, id):
	Comment.objects.get(id=id).delete()
	return redirect(reverse('course_list:comments', kwargs={'id':request.POST['course_id']}))
	# return redirect('/comments/' + request.POST['course_id'])

def show(request):
	all_users = User.objects.all()
	all_courses = Course.objects.all()
	courses_with_users = Course.objects.all()
	courses_with_users = Course.objects.annotate(total=Count('user'))
	context = {
		'users': all_users,
		'courses': all_courses, 
		'courses_with_users': courses_with_users,
	}
	return render(request, 'course_list/users_courses.html', context)

def add_user_course(request):
	Course.objects.add_user(user=request.POST['user'], course=request.POST['course'])
	return redirect(reverse('course_list:show'))