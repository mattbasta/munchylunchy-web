from django import http
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import bleach
import jingo


@login_required
def home(request):
    """Main example view."""
    data = {}  # You'd add data here that you're sending to the template.
    return jingo.render(request, 'single/home.html', data)


@csrf_exempt
def bleach_test(request):
    """A view outlining bleach's HTML sanitization."""
    allowed_tags = ('strong', 'em')

    data = {}

    if request.method == 'POST':
        bleachme = request.POST.get('bleachme', None)
        data['bleachme'] = bleachme
        if bleachme:
            data['bleached'] = bleach.clean(bleachme, tags=allowed_tags)

    return jingo.render(request, 'single/bleach.html', data)
