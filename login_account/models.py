# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length = 100, default ='')
	city = models.CharField(max_length = 100,default ='')
	website = models.URLField(default='')
	phone = models.IntegerField(default= 0)
	
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()

	def get_absolute_url(self):
		return reverse('post_list')

	def __str__(self):
		return self.title
		
# Create your models here.
def create_profile(sender, **kargs):
	if kargs['created']:
		user_profile= UserProfile.objects.create(user = kargs['instance'])

post_save.connect(create_profile,sender = User)



