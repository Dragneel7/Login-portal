# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from .models import UserDetails
from django.shortcuts import render,redirect, get_object_or_404
from .forms import UserDetailsForm
from django.http import HttpResponse

# Create your views here.

def dictionary(request):
	MYDIR = os.path.dirname(__file__)
	txt= open(os.path.join(MYDIR,'templates/login_app/dictionary_mod.txt')).read()
	return HttpResponse(txt)

def game(request):
	return render(request,'login_app/app.html',{})

def instruction(request):
	return render(request,'login_app/instruction.html',{})
	

def home(request):
	
	return render(request,'login_app/home.html',{})

def get_user(request,pk):
	user = get_object_or_404(UserDetails,pk=pk)
	
	return render(request,'login_app/login.html',{'user':user})


def user_new(request):
	
	if request.method == "POST":
		form = UserDetailsForm(request.POST)
	#	user = UserDetails.objects.get(user_name = form.user_name):
	#	if user.count()>0:
	#		return render(request,'login_app/user.html',{'form':form})
	
		
		if form.is_valid():
			user = form.cleaned_data.get('user_name')
			pas1 = form.cleaned_data.get('user_password') 
			if  UserDetails.objects.filter(user_name = user,user_password=pas1):
				return render(request,'login_app/login.html',{'user':user})
			elif UserDetails.objects.filter(user_name = user) and not(UserDetails.objects.filter(user_password=pas1)):	
				alert = "username taken"
				return render(request,'login_app/user.html',{'form':form,'alert':alert})	
			else:			
				UserDetails1 = form.save(commit = False)
			
				UserDetails1.save()
	                	return redirect('login_app:get_user',pk=UserDetails1.pk)
	

	else:
		form = UserDetailsForm()
		alert = "incorrect format"
		return render(request,'login_app/user.html',{'form':form,'alert':alert})


