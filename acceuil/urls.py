from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import *
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#app_name = "acceuil"

urlpatterns = [
	url(r'^contact/' , views.contact , name = 'contact'),
	url(r'^elements/' , views.elements , name = 'elements'),
	url(r'^home2/' , views.home2 , name = 'home2'),
    url(r'^', views.home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()