from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EmailManager, Email

# Create your views here.
def index(request):
	return render(request, 'email_app/index.html')

def validate(request):
	result = Email.objects.validate(email=request.POST['email'])
	if result[0] == 'True':
		messages.success(request, result[1])
		return redirect('/show')
	else:
		messages.error(request, result[1])
		return redirect('/')

def show(request):
	all_emails = Email.objects.all()
	formatted_times = Email.objects.format_time(Email.objects.values_list('created_at'))
	# Zip to tuple all the emails and formatted times
	emails = zip(all_emails, formatted_times)
	context = {
		'emails': emails
	}
	return render(request, 'email_app/email_list.html', context)

def delete(request, id):
	Email.objects.get(id=id).delete()
	return redirect('/show')