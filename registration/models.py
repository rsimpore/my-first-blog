# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User_extd(models.Model) :
	gender_choices = (
		(1 , "Mademoiselle"),
		(2 , "Madame"),
		(3 , "Monsieur"),
		)
	user = models.OneToOneField(User , on_delete = models.CASCADE)
	gender = models.PositiveSmallIntegerField(choices=gender_choices, null = True , blank = True)
	address = models.TextField(max_length = 200 , blank = True)
	postal_code = models.CharField(max_length = 10 , blank = True)
	city = models.CharField(max_length = 200 , blank = True)
	country = models.CharField(max_length = 200 , blank = True)
	birth_date = models.DateField(null = True , blank = True)

@receiver(post_save , sender = User)
def create_user_extd(sender , instance , created , **kwargs) :
	if created :
		User_extd.objects.create(user = instance)

@receiver(post_save , sender = User)
def save_user_extd(sender , instance , **kwargs) :
	instance.user_extd.save()