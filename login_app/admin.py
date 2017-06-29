from django.contrib import admin
from .models import UserDetails,UserStats
# Register your models here.

class UserStatsInline(admin.StackedInline):
	model = UserStats


class UserDetailsAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,           {'fields' : ['user_name']}),
	('Password',     {'fields' : ['user_password'],'class':['collapse']}),
	]
	
	inlines = [UserStatsInline]

admin.site.register(UserDetails,UserDetailsAdmin)
