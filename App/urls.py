from django.conf.urls import url, include, patterns
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'', include('homepage.urls', namespace = 'homepage')),
)
