from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('homepage.views',

    url(r'^$', 'index', name='home'),
    url(r'^(lt;short_id&gt;\w{6})$', 'redirect_original', name='redirectoriginal'), #?P&
    url(r'^makeshort/$', 'shorten_url', name='shortenurl'),
)
