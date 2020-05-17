from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^my_profile/' , views.my_profile , name = 'my_profile'),
	url(r'^register/' , views.register , name = 'register'),
	url(r'^edit_profile/' , views.edit_profile , name = 'edit_profile'),
]
