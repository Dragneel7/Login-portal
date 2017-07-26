
from django.conf.urls import url
from .import views


urlpatterns = [
	url(r'^$', views.user_new, name='user_new'),
#	url(r'^(?P<pk>\d+)/$',views.get_user, name='get_user'),
	url(r'^add/$','login_app.views.add', name = 'add'),	
#	url(r'^instructions/$',views.instruction,name='instruction'),
	url(r'^home/$',views.home, name='home'),
	url(r'^game/$',views.game, name='game'),
	url(r'^game/dictionary_mod.txt/$',views.dictionary,name='dictionary_mod'),
	url(r'^accounts/profile/$',views.github_login,name='github_login'),
	url(r'^stats/$',views.stats, name='stats'),
	url(r'^$',views.logout, name='logout'),
	url(r'^login_app/login_user/$',views.login_user,name='login'),
]
