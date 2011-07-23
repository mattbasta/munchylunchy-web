from django.conf.urls.defaults import *


urlpatterns = patterns('browserid.views',
    url(r'^logout$', 'logout_view', name='browserid.logout'),
    url(r'^login$', 'login_form', name='browserid.login'),
    url(r'^verify_login$', 'verify_login', name='browserid.verify_login'),
)

