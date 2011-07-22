from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

import jingo

# TODO: This should be a setting.
BROWSERID_INCLUDE_SCRIPT = 'https://browserid.org/include.js'

@login_required
def logout_view(request):
    logout(request)
    return HttpResponse('You are now logged out.')

def login_form(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    if 'single' in request.GET['next']:
        forward = 'single.home'
    elif 'group' in request.GET['next']:
        forward = 'group.home'
    else:
        forward = 'home.home'
    return jingo.render(request, 'browserid/login.html',
        {
            'browserid_include_script': BROWSERID_INCLUDE_SCRIPT,
            'forward': forward
        }
        )

@require_POST
def verify_login(request):
    user = authenticate(assertion=request.POST['assertion'],
                        host=request.META['SERVER_NAME'],
                        port=request.META['SERVER_PORT'])
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse(request.POST['forward']))
        else:
            return HttpResponse('your account is disabled.')
    else:
        return HttpResponse('access denied')

