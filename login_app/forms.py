
from django import forms
from .models import UserDetails ,UserStats
#from django.forms import formset_factory

class UserDetailsForm(forms.ModelForm):
#	user_password = forms.CharField(widget=forms.PasswordInput)
	user_name = forms.CharField(widget=forms.TextInput(attrs = {'placeholder' : 'Username'}))
	user_password = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder' : 'Password'}))
	
	class Meta:
		model = UserDetails
		fields = ('user_name','user_password',)
	#	widgets = {
	#	    'user_name':forms.TextInput(attr={'placeholder':'UserName'}),
#		user_password = forms.CharField(widget=forms.PasswordInput)
	
#		widgets = {
#			'user_password':forms.PasswordInput(),
	#	}

#UserStatsFormset =formset_factory(UserDetails,UserStats,
#	)
#class UserStatsForm(forms.ModelForm):
#	class Meta:
#		model=UserStats
#		fields = ('user_stat',)
