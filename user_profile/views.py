# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate
from django.contrib import messages
from django.conf import settings
import urllib, urllib2, json

# Create your views here.
def my_profile(request):
	return render(request , 'user_profile/profile.html')

def register(request):
# Validate the reCAPTCHA
	recaptcha_response = request.POST.get('g-recaptcha-response')
	url = 'https://www.google.com/recaptcha/api/siteverify'
	values = {
		'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		'response': recaptcha_response
	}
	data = urllib.urlencode(values)
	req = urllib2.Request(url , data)
	response = urllib2.urlopen(req)
	result = json.load(response)

# Test if the reCAPTCHA is valid
	if result['success']:
# Test if the form has been filled by user
		if request.method == 'POST':
# Collect infos from the form
			gender = request.POST['gender']
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			email = request.POST['email']
			birth_date = request.POST['birth_date']
			address = request.POST['address']
			postal_code = request.POST['postal_code']
			city = request.POST['city']
			country = request.POST['country']
			password = request.POST['password']

# Create the user with basic infos (username + password)
			user = User.objects.create_user(email , password)
# Update remaining user infos
			user.first_name = first_name
			user.last_name = last_name
			user.email = email
# Update additional infos
			user.user_extd.gender = gender
			user.user_extd.birth_date = birth_date
			user.user_extd.address = address
			user.user_extd.postal_code = postal_code
			user.user_extd.city = city
			user.user_extd.country = country
# Save user infos
			user.save()
# Login user
			login(request , user)
			return render(request , 'acceuil/index.html')

		else :
			return render(request , 'user_profile/register.html')
	else :
		return render(request , 'user_profile/register.html')

def edit_profile(request):
# Test if the form has been filled by user
	if request.method == 'POST':
# Collect infos from the form
		gender = request.POST['gender']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		birth_date = request.POST['birth_date']
		address = request.POST['address']
		postal_code = request.POST['postal_code']
		city = request.POST['city']
		country = request.POST['country']

# Update user infos
		user = request.user
		user.first_name = first_name
		user.last_name = last_name
		user.email = email
		user.username = email
# Update additional infos
		user.user_extd.gender = gender
		user.user_extd.birth_date = birth_date
		user.user_extd.address = address
		user.user_extd.postal_code = postal_code
		user.user_extd.city = city
		user.user_extd.country = country
# Save user infos
		user.save()
		messages.success(request , "Vos informations ont bien été mises à jour")
		return render(request , 'user_profile/profile.html')
	else :
		return render(request , 'user_profile/edit_profile.html')