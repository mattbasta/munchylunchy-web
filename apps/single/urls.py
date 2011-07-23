from django.conf.urls.defaults import *


urlpatterns = patterns('single.views',
    url(r'^$', 'home', name='single.home'),
    url(r'^get_questions', 'get_questions', name='single.get_questions'),
    url(r'^set_likes', 'set_likes', name='single.set_likes'),
    url(r'^decide', 'decide', name='single.decide'),
)
