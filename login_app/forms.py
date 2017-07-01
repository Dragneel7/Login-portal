
from django import forms
from .models import UserDetails

class UserDetailsForm(forms.ModelForm):
	user_password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = UserDetails
		fields = ('user_name','user_password',)
	#	widgets = {
	#	    'user_name':forms.TextInput(attr={'placeholder':'UserName'}),

	
