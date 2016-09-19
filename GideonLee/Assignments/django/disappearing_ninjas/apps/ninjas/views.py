from django.shortcuts import render, redirect

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
	else:
		ninja = ['april']
	context = {
		'ninjas': ninja
	}
	return render(request, 'ninjas/show.html', context)
