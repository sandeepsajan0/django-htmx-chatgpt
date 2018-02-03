# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from login_account.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import NewsForm,Posts
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.core.mail import EmailMessage
from login_account.tokens import account_activation_token
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login, authenticate


def hello(request):
    number=[1,2,3,4,5]
    name="Sandeep Chauhan"
    args = {'myname':name,'Number':number}
    return render(request, 'login_account/home.html', args)

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your blog account.'
			message = render_to_string('acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user)})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
				mail_subject, message,to=[to_email]
			)
			email.send()
			return HttpResponse('Please confirm your email address to complete the registration')
	else:
		form = RegistrationForm()
	args = {'form': form}
	return render (request,'login_account/reg_form.html',args)
@login_required
def profile(request):
	args = {'user': request.user}
	return render (request,'login_account/profile.html',args)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #login(request, user)
        # return redirect('home')
        return redirect('/login/home1')
    else:
        return HttpResponse('Activation link is invalid!')

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
	model = Posts
	template_name = 'login_account/post_list.html'

@login_required
def post_detail(request,*args, **kwargs):
	blog_post = get_object_or_404(Posts, pk=kwargs.get("pk"))
	if blog_post.author == request.user:
		
		return render(request,'login_account/post_detail.html',{'post':blog_post})
	else:
		return redirect('/login/public_page/')
		

@login_required	
def news_poster(request):
    if request.method == 'POST':
        
        form = NewsForm(request.POST)
        if form.is_valid():
            news_item = form.save(commit = False)
            news_item.author = request.user  # User posting the form
            news_item.save()
        return redirect('/login/public_page/')
    else:
        form = NewsForm()
    return render(request,'login_account/post_new.html', {'form': form})



    

class BlogUpdateView(UpdateView):
    model = Posts
    fields = ['title', 'text']
    template_name = 'login_account/post_edit.html'

class BlogDeleteView(DeleteView):
    model = Posts
    template_name = 'login_account/post_delete.html'
    success_url = reverse_lazy('post_list') 
# Create your views here.
