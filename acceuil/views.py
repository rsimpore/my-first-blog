# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
import urllib, urllib2, json

# Create your views here.
def home(request):
	return render(request , 'acceuil/index.html')

def elements(request):
	return render(request , 'acceuil/elements.html')

def home2(request):
	return render(request , 'acceuil/index-old.html')

def contact(request):
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
			last_name = request.POST['last_name']
			first_name = request.POST['first_name']
			email = request.POST['email']
			message = request.POST['message']
# Send email
			email_to_send = EmailMessage(
				'Vous avez reçu un message de la part de {} {} - {}'.format(first_name , last_name , email),
				message,
				settings.EMAIL_HOST_USER,
#				[settings.EMAIL_HOST_USER],
				['camaret.c@gmail.com'],
				[],
				reply_to = [email],				
				)
			email_to_send.send(fail_silently = False)
			messages.success(request , "Votre message a bien été envoyé.")
			return render(request , 'acceuil/contact.html')

		else :
			return render(request , 'acceuil/contact.html')
	else :
		return render(request , 'acceuil/contact.html')