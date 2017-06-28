
from django import forms
from .models import UserDetails

class UserDetailsForm(forms.ModelForm):
	class Meta:
		model = UserDetails
		fields = ('user_name','user_password',)
