import urllib
import urllib2
import logging

from django.contrib.auth.models import User
from django.utils import simplejson as json

from api.harness import API


class BrowserIdBackend(object):
    supports_object_permissions = False
    supports_anonymous_user = False

    def authenticate(self, assertion=None, host='munchylunchy.com', port=80):

        result = API.verify_user(assertion=assertion)
        logging.error(str(result))
        if result['result'] == 'okay':
            email = result['email']
            token = result['token']
            try:
                user = User.objects.get(username=email)
            except User.DoesNotExist:
                user = User(username=email, password=token)
                user.save()
            return user
        logging.error("user login failed: %s" % repr(result))
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

