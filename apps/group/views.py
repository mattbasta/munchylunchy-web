from django import http
from django.contrib.auth.decorators import login_required

import bleach
import jingo


@login_required
def home(request):
    data = {}
    return jingo.render(request, 'group/home.html', data)

