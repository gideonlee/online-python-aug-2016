from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^all$', views.show),
	url(r'^(?P<name>\w+)$', views.show_one),
]