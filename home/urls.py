from django.conf.urls import patterns, include, url

urlpatterns = patterns('home.views',

    url(r'^$', 'index', name='home'),
    url(r'^(lt;short_id&gt;\w{6})$', 'redirect_original', name='redirectoriginal'), # Erro of regex here
    url(r'^makeshort/$', 'shorten_url', name='shortenurl'),
)
