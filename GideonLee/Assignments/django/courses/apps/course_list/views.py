from django.shortcuts import render, redirect
from .models import CourseManager, Course, Comment

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
		print new_course[1]

	return redirect('/')

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
	return redirect('/')

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
	return redirect('/comments/'+id)

# Allows the user to delete a comment about the course 
def delete_comment(request, id):
	Comment.objects.get(id=id).delete()
	return redirect('/comments/' + request.POST['course_id'])