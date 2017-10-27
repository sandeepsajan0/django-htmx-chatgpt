# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from login_account.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

def hello(request):
    number=[1,2,3,4,5]
    name="Sandeep Chauhan"
    args = {'myname':name,'Number':number}
    return render(request, 'login_account/home.html', args)

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/login')
	else:
		form = RegistrationForm()
		args = {'form': form}
		return render (request,'login_account/reg_form.html',args)

def profile(request):
	args = {'user': request.user}
	return render (request,'login_account/profile.html',args)


def edit_profile(request):
	if request.method == "POST":
		form = EditProfileForm(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			return redirect('/login/profile')
	else:
		form = EditProfileForm(instance = request.user)
		args = {'form': form}
		return render (request,'login_account/edit_profile.html',args)
# Create your views here.
