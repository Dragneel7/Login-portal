# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import UserDetails
from django.shortcuts import render,redirect, get_object_or_404
from .forms import UserDetailsForm


# Create your views here.

def game(request):
	return render(request,'login_app/app.html',{})

def instruction(request):
	return render(request,'login_app/instruction.html',{})
	

def home(request):
	
	return redirect('login_app:get_user',pk=1)

def get_user(request,pk):
	user = get_object_or_404(UserDetails,pk=pk)
	
	return render(request,'login_app/login.html',{'user':user})


def user_new(request):
	
	if request.method == "POST":
		form = UserDetailsForm(request.POST)
		if form.is_valid():
			UserDetails = form.save(commit = False)
			
			UserDetails.save()
	                return redirect('login_app:get_user',pk=UserDetails.pk)
	

	else:
		form = UserDetailsForm()
		return render(request,'login_app/user.html',{'form':form})


