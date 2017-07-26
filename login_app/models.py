from django.contrib.auth.models import User

from django.db import models

# Create your models here.



class UserStats(models.Model):
	userdetails = models.ForeignKey(User)
	user_stat = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.user_stat
