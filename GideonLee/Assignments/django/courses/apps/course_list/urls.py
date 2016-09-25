from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add$', views.add_course, name='add'),
	url(r'^delete/(?P<id>\d+)$', views.confirm_delete, name='confirm_delete'),
	url(r'^delete$', views.delete, name='delete'),
	url(r'^comments/(?P<id>\d+)$', views.comments, name='comments'),
	url(r'^post_comment/(?P<id>\d+)$', views.post_comment, name='post_comment'),
	url(r'^delete_comment/(?P<id>\d+)$', views.delete_comment, name='delete_comment')
]