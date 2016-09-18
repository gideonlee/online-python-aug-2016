from django.shortcuts import render, HttpResponse, redirect
#try removing httpresposne when using context

# Create your views here.
def index(request):
	return render(request, 'survey/index.html')

def result(request):
	return render(request, 'survey/result.html')

def process(request):
	if request.method == 'POST':
		try: 
			request.session['counter'] += 1 
		except:
			request.session['counter'] = 1
		request.session['name'] = request.POST['name']
		request.session['email'] = request.POST['email']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comments'] = request.POST['comments']
		return redirect('/result')

def go_back(request):
	if request.method == 'GET':
		del request.session['name']
		del request.session['email']
		del request.session['location']
		del request.session['language']
		del request.session['comments']
		return redirect('/')