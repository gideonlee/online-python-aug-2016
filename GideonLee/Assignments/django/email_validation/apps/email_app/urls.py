from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^validate$', views.validate, name='validate'),
	url(r'^show$', views.show, name='show'),
	url(r'^(?P<id>\d+)/delete', views.delete, name='delete'), 
]