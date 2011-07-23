import json

from django import http
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

import jingo

from api.harness import API, User


@login_required
def home(request):
    data = {}  # You'd add data here that you're sending to the template.
    return jingo.render(request, 'group/home.html', data)

@login_required
def decide(request):
    you = User(request.user.username, request.user.password)
    result = API.places_decide(you, request.GET['latitude'], request.GET['longitude'])

    data = { 'decision': result['decision'] }
    return jingo.render(request, 'group/decide.html', data)

@login_required
def dashboard(request, group_id):
    return jingo.render(request, 'group/dashboard.html', data)
