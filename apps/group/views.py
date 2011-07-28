import json

from django import http
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import jingo

from api.harness import API, User


@login_required
def home(request): # create
    data = {}  # You'd add data here that you're sending to the template.
    you = User(request.user.username, request.user.password)
    group = API.group_create(you)
    if not group:
        logout(request)
        return HttpResponseRedirect(reverse('group.home'))

    group_id = group['group_id']
    return HttpResponseRedirect(reverse('group.get_info', args=[group_id]))

@login_required
def get_info(request, group_id):
    data = {'groupid': group_id}
    return jingo.render(request, 'group/ask.html', data)


@login_required
def dashboard(request, group_id):
    you = User(request.user.username, request.user.password)

    if 'latitude' in request.GET:
        latitude = request.GET['latitude']
    else:
        latitude = '0'

    if 'longitude' in request.GET:
        longitude = request.GET['longitude']
    else:
        longitude = '0'
    data = API.group_register(you, group_id, latitude, longitude)
    if not data or data['registered'] == 'new':
        return HttpResponseRedirect(reverse('group.get_info', args=[group_id]))
    elif data['registered'] == 'yes':
        data['groupid'] = group_id
        return jingo.render(request, 'group/dashboard.html', data)

    return HttpResponseBadRequest()

@login_required
def async_list(request, group_id):
    data = {}
    you = User(request.user.username, request.user.password)
    restaurants = API.group_poll(you, group_id)

    return HttpResponse(json.dumps(restaurants))
