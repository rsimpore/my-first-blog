# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import *
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.conf import settings
from acceuil.models import *

# Create your views here.


def home(request):
	return render(request, 'acceuil/index.html')

def association(request):
	return render(request, 'acceuil/association.html')