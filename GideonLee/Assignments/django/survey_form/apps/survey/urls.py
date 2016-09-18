from django.conf.urls import url
from . import views

urlpatterns = [
	# If you don't include the $ in r'^$', everything will get caught by views.index 
	url(r'^$', views.index),
	url(r'^result$', views.result),
	url(r'^surveys/process$', views.process),
	url(r'^surveys/new$', views.go_back),
]