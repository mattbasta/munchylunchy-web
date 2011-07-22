from django.conf.urls.defaults import *


urlpatterns = patterns('browserid.views',
    url(r'^logout$', 'logout_view'),
    url(r'^login$', 'login_form'),
    url(r'^verify_login$', 'verify_login'),
)

