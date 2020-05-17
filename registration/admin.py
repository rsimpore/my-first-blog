# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import User_extd

# Register your models here.
class User_extdInline(admin.StackedInline):
	model = User_extd
	can_delete = False
	verbose_name_plural = 'User_extd'
	fk_name = 'user'

class CustomUserAdmin(UserAdmin):
	inlines = (User_extdInline, )

	def get_inline_instances(self , request , obj = None):
		if not obj:
			return list()
		return super(CustomUserAdmin , self).get_inline_instances(request , obj)

admin.site.unregister(User)
admin.site.register(User , CustomUserAdmin)