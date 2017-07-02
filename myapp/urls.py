from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'',include('login_app.urls',namespace="login_app")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',auth_views.login, name='login'),
    url(r'^logout/$',auth_views.logout, name='logout'),
    url(r'^oauth/',include('social_django.urls',namespace='social')),

]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'login_app:home'
