from django.shortcuts import render, redirect
import random 
import string

alphanum = string.ascii_lowercase
for number in range(10):
	alphanum += str(number)
# print random.choice(alphanum)

# Create your views here.
def index(request):
	# request.session.clear()
	if 'random_word' not in request.session:
		request.session['random_word'] = 'Press Generate'
	return render(request, 'rand_word/index.html')

def generate(request):
	try:
		request.session['attempt_number'] += 1
	except:
		request.session['attempt_number'] = 1

	random_word = ''
	for num in range(14):
		random_word += random.choice(alphanum)
	request.session['random_word'] = random_word
	return redirect('/')