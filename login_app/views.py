# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from .models import UserStats
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect, get_object_or_404,render_to_response
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
#from allauth.account.signals import user_signed_up
#from django.dispatch import reciever
# Create your views here.

def dictionary(request):
	MYDIR = os.path.dirname(__file__)
	txt= open(os.path.join(MYDIR,'templates/login_app/dictionary_mod.txt')).read()
	return HttpResponse(txt)


def user_new(request):
	
	if request.method == 'POST':
		form = UserForm(request.POST)
		print form.is_valid
		print form.errors
		if form.is_valid:
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')	
			user = User.objects.create(username = username)
			user.set_password(password)
			user.save()
			user = authenticate(username = username, password = password)
			login(request,user)
			return render(request,'login_app/home.html',{'user':request.user.username})	

	else:
		form = UserForm()
	
		return render(request,'login_app/user.html',{'form_signup':form,'form_login':form})

def login_user(request):
	if request.method == 'POST':
		form = AuthenticationForm(request,request.POST)
		print form
		print "hello"
		if form.is_valid:
			#print form.cleaned_data
			#username = form.cleaned_data.get('username')
			#print username		
			#password = form.cleaned_data.get('password')
		 	#print password
			#user = User.objects.get(username = username)
			#password = user.set_password(user.password)
			#user = authenticate(username = username , password = password)
		
			login(request,form.get_user())
			return render(request,'login_app/home.html',{'user':request.user.username})

	else:
		form = UserForm()
		print form 	
		return render(request,'login_app/user.html',{'form_login':form})

@login_required

def logout(request):
	logout(request)

	return render(request,'login_app/user.html',{})



def home(request):
#	user = request.session['username']	
	return render(request,'login_app/home.html',{'user':request.user.username})

#@reciever(user_signed_up)
def github_login(request):
	user = request.user.first_name
	if not(User.objects.filter(user_name = user)):
		q = UserDetails(user_name = user,user_password = "")
		q.save()
	request.session['username'] = user
	return render(request,'login_app/home.html',{'user':request.session['username']})

def game(request):
	return render(request,'login_app/app.html',{'user':request.user.username})

		
def add(request):
	stat = request.GET.get('text')
	q = User.objects.get(username = request.user.username)
	q.userstats_set.create(user_stat=stat)
	return HttpResponse('done')	

def stats(request):
	q = User.objects.get(username = request.user.username)
	stats = q.userstats_set.all().order_by('-id')
	return render(request,'login_app/stats.html',{'stats':stats})


