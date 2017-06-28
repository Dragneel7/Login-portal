
from django.conf.urls import url
from .import views

urlpatterns = [
	url(r'^user/new/$', views.user_new, name='user_new'),
	url(r'^user/(?P<pk>\d+)/$',views.get_user, name='get_user'),
]
