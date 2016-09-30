from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register$', views.register, name='register'),
	url(r'^login$', views.login, name='login'),
	url(r'^books$', views.home, name='home'),
	url(r'^books/add$', views.add, name='add'),
	url(r'^books/process$', views.process, name='process'),
	url(r'^books/(?P<id>\d+)$', views.show_book, name='show_book'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^users/(?P<id>\d+)$', views.show_user, name='show_user'),
	url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
]