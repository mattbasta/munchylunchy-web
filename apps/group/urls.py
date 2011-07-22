from django.conf.urls.defaults import *


urlpatterns = patterns('group.views',
    url(r'^$', 'home', name='group.home'),
)
