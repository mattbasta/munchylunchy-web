from django.conf.urls.defaults import *


urlpatterns = patterns('single.views',
    url(r'^$', 'home', name='single.home'),
    url(r'bleach', 'bleach_test', name='single.bleach'),
)
