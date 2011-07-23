from django.conf.urls.defaults import *


urlpatterns = patterns('group.views',
    url(r'^$', 'home', name='group.home'),
    url(r'^getinfo/(?P<group_id>\w+)$', 'get_info', name='group.get_info'),
    url(r'^dashboard/(?P<group_id>\w+)', 'dashboard', name='group.dashboard'),
    url(r'^asynclist/(?P<group_id>\w+)', 'async_list', name='group.async_list'),
)
