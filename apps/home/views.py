from django import http
from django.views.decorators.csrf import csrf_exempt

import bleach
import jingo


def home(request):
    """Main example view."""
    data = {}  # You'd add data here that you're sending to the template.
    return jingo.render(request, 'home/home.html', data)

