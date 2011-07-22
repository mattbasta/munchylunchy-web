# This is your project's main settings file that can be committed to your
# repo. If you need to override a setting locally, use settings_local.py

from funfactory.settings_base import *

# Logging
SYSLOG_TAG = "munchylunchy-web"  # Make this unique to your project.


# Bundles is a dictionary of two dictionaries, css and js, which list css files
# and js files that can be bundled together by the minify app.
MINIFY_BUNDLES = {
    'css': {
        'common': (
            'css/main.css',
        ),
    },
    'js': {
        'main': (
            'js/libs/jquery-1.4.4.min.js',
        ),
    }
}


INSTALLED_APPS = list(INSTALLED_APPS) + [
    # Example code. Can (and should) be removed for actual projects.
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'single',
    'browserid',
]


AUTHENTICATION_BACKENDS = (
    'browserid.backends.BrowserIdBackend',
)

LOGIN_URL = '/accounts/login'
LOGOUT_URL = '/accounts/logout'
LOGIN_REDIRECT_URL = '/single'
LOGOUT_REDIRECT_URL = '/'

PREPEND_WWW = False

APPEND_SLASH = False

SUPPORTED_NONLOCALES = list(SUPPORTED_NONLOCALES) + [
    'accounts',
]

# Tells the extract script what files to look for L10n in and what function
# handles the extraction. The Tower library expects this.

# # Use this if you have localizable HTML files:
# DOMAIN_METHODS['lhtml'] = [
#    ('**/templates/**.lhtml',
#        'tower.management.commands.extract.extract_tower_template'),
# ]

# # Use this if you have localizable HTML files:
# DOMAIN_METHODS['javascript'] = [
#    # Make sure that this won't pull in strings from external libraries you
#    # may use.
#    ('media/js/**.js', 'javascript'),
# ]
