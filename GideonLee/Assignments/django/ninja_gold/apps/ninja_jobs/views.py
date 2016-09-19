from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

# Create your views here.
def index(request):
	# request.session.clear()
	if 'messages' not in request.session:
		request.session['messages'] = []
	if 'gold' not in request.session:
		request.session['gold'] = 0
	return render(request, 'ninja_jobs/index.html')

def process(request):
	if request.method == 'POST':
		time = strftime('(%Y/%d/%m %I:%M %p)', gmtime())
		
		if request.POST['type_of_job'] == 'farm' or request.POST['type_of_job'] == 'cave' or request.POST['type_of_job'] == 'house': 
			if request.POST['type_of_job'] == 'farm':
				amount = int(round(random.uniform(10, 20)))
			elif request.POST['type_of_job'] == 'cave':
				amount = int(round(random.uniform(5, 10)))
			elif request.POST['type_of_job'] == 'house':
				amount = int(round(random.uniform(2, 5)))
			request.session['gold'] += amount
			request.session['messages'].insert(0, 'Earned ' + str(amount) + ' gold from the ' + request.POST['type_of_job'] + '! ' + time)	
		
		if request.POST['type_of_job'] == 'casino':
			amount = int(round(random.uniform(-50, 50)))
			request.session['gold'] += amount
			if amount > 0: 
				request.session['messages'].insert(0, 'Entered a casino and won ' + str(abs(amount)) + ' gold! Yay! ' + time)
			else:
				request.session['messages'].insert(0, 'Entered a casino and lost ' + str(abs(amount)) + ' gold! ... Ouch ... ' + time)	
	return redirect('/')