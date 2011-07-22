from django.conf.urls.defaults import *


urlpatterns = patterns('single.views',
    url(r'^$', 'home', name='single.home'),
)
