from django.contrib.auth.models import User
from django import forms

#from django.forms import formset_factory

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs = {'placeholder' : 'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder' : 'Password'}))

	class Meta:
		model = User
		fields = ('username','password')

	def clean(self, *args, **kwargs):
		username = self.cleaned_data['username']
		return super(UserForm, self).clean(*args, **kwargs)

	
