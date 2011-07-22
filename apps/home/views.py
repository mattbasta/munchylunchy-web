from django import http

import jingo

def home(request):
    data = {}
    return jingo.render(request, 'home/home.html', data)

