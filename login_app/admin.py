from django.contrib import admin


from .models import *
# Register your models here.

class UserStatsInline(admin.ModelAdmin):
	model = UserStats


#class UserAdmin(admin.ModelAdmin):
#	fieldsets = [
#	(None,           {'fields' : ['username']}),
#	('Password',     {'fields' : ['password'],'classes':['collapse']}),
#	]
	
#	inlines = [UserStatsInline]

#admin.site.register(UserAdmin)
admin.site.register(UserStats)
