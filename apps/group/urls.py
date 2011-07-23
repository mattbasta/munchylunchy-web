from django.conf.urls.defaults import *


urlpatterns = patterns('group.views',
    url(r'^$', 'home', name='group.home'),
    url(r'^decide', 'decide', name='group.decide'),
    url(r'^(?P<group_id>\d+)', 'dashboard', name='group.dashboard'),
)
