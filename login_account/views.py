# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from login_account.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post
from django.urls import reverse_lazy

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
			return redirect('/login/login_account')
	else:
		form = RegistrationForm()
	args = {'form': form}
	return render (request,'login_account/reg_form.html',args)
@login_required
def profile(request):
	args = {'user': request.user}
	return render (request,'login_account/profile.html',args)

@login_required
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

@login_required
def public_page(request):
	number=[1,2,3,4,5]
	name="Sandeep Chauhan"
	args = {'myname':name,'Number':number}
	return render (request,'login_account/public_page.html', args)


class BlogListView(ListView):
	model = Post
	template_name = 'login_account/post_list.html'

class BlogDetailView(DetailView):
	model = Post
	template_name = 'login_account/post_detail.html'
	
class BlogCreateView(CreateView):
    model = Post
    template_name = 'login_account/post_new.html'
    fields = '__all__'
# Create your views here.
