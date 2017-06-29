

from django.db import models

# Create your models here.

class UserDetails(models.Model):
	user_name = models.CharField(max_length = 100)
	user_password = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.user_name

class UserStats(models.Model):
	user_stat = models.ForeignKey(UserDetails)	
	
	
