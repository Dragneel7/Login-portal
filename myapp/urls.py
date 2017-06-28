from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'',include('login_app.urls',namespace="login_app")),
    url(r'^admin/', include(admin.site.urls)),
]
