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
    return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

def login_form(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    if 'single' in request.GET['next']:
        forward = 'single.home'
    elif 'group/dashboard/' in request.GET['next']:
        forward = 'group.dashboard:' + request.GET['next'][-4:]
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
            if 'group.dashboard' in request.POST['forward']:
                fwd = request.POST['forward'].split(':')
                url = reverse(fwd[0], args=[fwd[1]])
            else:
                url = reverse(request.POST['forward'])

            return HttpResponseRedirect(url)
        else:
            return HttpResponse('your account is disabled.')
    else:
        return HttpResponse('access denied')

