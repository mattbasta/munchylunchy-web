from django import http
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import bleach
import jingo

@login_required
def home(request):
    """Main example view."""
    data = {}  # You'd add data here that you're sending to the template.
    return jingo.render(request, 'home/home.html', data)

