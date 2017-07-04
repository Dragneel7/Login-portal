

from django.db import models

# Create your models here.

class UserDetails(models.Model):
	user_name = models.CharField("UserName",max_length = 100)
	user_password = models.CharField("PassWord",max_length = 50)

	def __unicode__(self):
		return self.user_name
	

class UserStats(models.Model):
#	userdetails = models.ForeignKey(UserDetails)
	user_stat = models.CharField(max_length=200)
