"""multiple_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include 

urlpatterns = [
	url(r'^', include('apps.rand_word.urls', namespace='rand_word')),
	url(r'ninjas/', include('apps.ninjas.urls', namespace='ninjas')),
	url(r'ninjas/game', include('apps.ninja_jobs.urls', namespace='ninja_jobs')),
	url(r'courses/', include('apps.course_list.urls', namespace='course_list')),
	url(r'user/', include('apps.login_registration.urls', namespace='user')),
]
