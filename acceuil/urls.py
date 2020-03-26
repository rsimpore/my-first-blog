from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import *
from acceuil import views

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
     url(r'^', views.home, name='home'),
     url(r'^acceuil/association', views.association, name='association'),
]
