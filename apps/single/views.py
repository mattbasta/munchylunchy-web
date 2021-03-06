import json

from django import http
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import jingo

from api.harness import API, User


@login_required
def home(request):
    you = User(request.user.username, request.user.password)
    response = API.verify_token(you)
    if (not response or
        "result" not in response or
        response["result"] != "okay"):

        logout(request)
        return HttpResponseRedirect(reverse('single.home'))

    data = {}  # You'd add data here that you're sending to the template.
    return jingo.render(request, 'single/home.html', data)

@login_required
def get_questions(request):
    you = User(request.user.username, request.user.password)
    response = API.taste_query(you, request.POST['latitude'],
                               request.POST['longitude'])
    if not response:
        logout(request)
        return HttpResponseRedirect(reverse('single.get_questions'))

    if response['result'] != 'okay':
        return HttpResponse(json.dumps(response))

    clean_names = [settings.FOOD_STYLES[i] for i in response['tastes']]

    response['tastes_pretty'] = clean_names[:response['to_ask']]

    return HttpResponse(json.dumps(response))

@login_required
@require_POST
def set_likes(request):
    you = User(request.user.username, request.user.password)
    result = API.taste_set(you, request.POST['taste'], request.POST['likes'] == 'yep')

    return HttpResponse(result)

@login_required
def decide(request):
    you = User(request.user.username, request.user.password)
    result = API.places_decide(you, request.GET['latitude'], request.GET['longitude'])
    if not result:
        logout(request)
        return HttpResponseResult(reverse('single.decide'))

    reasons = []
    for reason in result['reasons']:
        if reason.startswith('like:'):
            reasons.append('You like %s.' % settings.FOOD_STYLES[reason[5:]])
        elif reason == 'distance':
            reasons.append("It's nearby.")
        elif reason == 'great_rating':
            reasons.append("It has a great rating of %.1f stars on Yelp." % result['stars'])
        elif reason == 'good_rating':
            reasons.append('It has a good rating of %.1f stars on Yelp.' % result['stars'])
        elif reason == 'notrecent':
            reasons.append("We haven't suggested this to you in a while.")

    data = { 'decision': result['business']['name'],
             'reasons': reasons,
             'latitude': result['business']['location']['coordinate']['latitude'],
             'longitude': result['business']['location']['coordinate']['longitude'],
             'address': result['business']['location']['display_address'],
             'phone': result['business']['display_phone']}
    return jingo.render(request, 'single/decide.html', data)
