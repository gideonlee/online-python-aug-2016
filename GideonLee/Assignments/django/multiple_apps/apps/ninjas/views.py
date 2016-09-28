from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request): 
	return render(request, 'ninjas/index.html')

def show(request):
	context = {
		'ninjas': ['michelangelo', 'raphael', 'donatello', 'leonardo']
	}
	return render(request, 'ninjas/show.html', context)

def show_one(request, name):
	if name == 'orange': 
		ninja = ['michelangelo']
	elif name == 'red':
		ninja = ['raphael']
	elif name == 'purple':
		ninja = ['donatello']
	elif name == 'blue':
		ninja = ['leonardo']
	elif name == 'game':
		return redirect('/ninjas/game')
	else:
		ninja = ['april']
	context = {
		'ninjas': ninja
	}
	return render(request, 'ninjas/show.html', context)
