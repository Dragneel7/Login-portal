# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from .models import UserDetails
from django.shortcuts import render,redirect, get_object_or_404,render_to_response
from .forms import UserDetailsForm,UserStats
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import auth
#from allauth.account.signals import user_signed_up
#from django.dispatch import reciever
# Create your views here.

def dictionary(request):
	MYDIR = os.path.dirname(__file__)
	txt= open(os.path.join(MYDIR,'templates/login_app/dictionary_mod.txt')).read()
	return HttpResponse(txt)

#def instruction(request):
#	return render(request,'login_app/instruction.html',{})
	
#def get_user(request,pk):
#	user = get_object_or_404(UserDetails,pk=pk)
	
#	return render(request,'login_app/login.html',{'user':user})


def user_new(request):
	
	if request.method == "POST":
		form = UserDetailsForm(request.POST)
	#	user = UserDetails.objects.get(user_name = form.user_name):
	#	if user.count()>0:
	#		return render(request,'login_app/user.html',{'form':form})
	
		
		if form.is_valid():
			user = form.cleaned_data.get('user_name')
			pas1 = form.cleaned_data.get('user_password') 
			request.session['username'] = user

			if  UserDetails.objects.filter(user_name = user,user_password=pas1):
			
				return render(request,'login_app/home.html',{'user':request.session['username']})
			elif UserDetails.objects.filter(user_name = user) and not(UserDetails.objects.filter(user_password=pas1)):	
				alert = "username taken"
				return render(request,'login_app/user.html',{'form':form,'alert':alert})	
			else:			
				UserDetails1 = form.save(commit = False)
			        
				UserDetails1.save()
				
	                	return render(request,'login_app/home.html',{'user':request.session['username']})
	

	else:
		form = UserDetailsForm()
	
		return render(request,'login_app/user.html',{'form':form})


@login_required

def logout(request):
	auth.logout(request)

	return render(request,'login_app/user.html',{})



def home(request):
        user = request.session['username']	
	return render(request,'login_app/home.html',{'user':user})

#@reciever(user_signed_up)
def github_login(request):
	user = request.user.first_name
	request.session['username'] = user
	return render(request,'login_app/home.html',{'user':request.session['username']})

def game(request):
	user = request.session['username']
	return render(request,'login_app/app.html',{'user':user})

		
def add(request):
	stat = request.GET.get('text')
	q = UserDetails.objects.get(user_name = request.session['username'])
	q.userstats_set.create(user_stat=stat)
	return HttpResponse('done')	

def stats(request):
	q = UserDetails.objects.get(user_name = request.session['username'])
	stats = q.userstats_set.all().order_by('-id')
	return render(request,'login_app/stats.html',{'stats':stats})


