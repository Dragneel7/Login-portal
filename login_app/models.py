

from django.db import models

# Create your models here.

class UserDetails(models.Model):
	user_name = models.CharField(max_length = 100)
	user_password = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.user_name

class UserStats(models.Model):
	user = models.ForeignKey(UserDetails)
	user_stat = models.CharField(max_length=200)	

	def __init__(self,user_stat=None,*args,**kwargs):
		self.user_stat = user_stat or self.user_stat
	
	def __unicode__(self):
		return self.user_stat	
