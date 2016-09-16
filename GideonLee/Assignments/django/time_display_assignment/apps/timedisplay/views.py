from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
	now = datetime.now()
	context = {
		'day_of_the_week': now.strftime('%A'),
		'month_year': now.strftime('%b %Y'),
		'day': now.day,
		'time': now.time
	}
	return render(request, 'timedisplay/index.html', context)