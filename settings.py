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
        'common': (
            'js/libs/jquery-1.6.2.min.js',
            'js/common.js',
        ),
        'single': (
            'js/single.js',
        ),
        'group': (
            'js/group.js',
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
    'group',
    'browserid',
]


AUTHENTICATION_BACKENDS = (
    'browserid.backends.BrowserIdBackend',
)

LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

PREPEND_WWW = False

APPEND_SLASH = False

SUPPORTED_NONLOCALES = list(SUPPORTED_NONLOCALES) + [
    'login',
    'logout',
    'verify_login',
]

FOOD_STYLES = {
    "afghani": "Afghani",
    "african": "African",
    "newamerican": "New American",
    "tradamerican": "Traditional American",
    "argentine": "Argentine",
    "asianfusion": "Asian Fusion",
    "bbq": "BBQ",
    "basque": "Basque",
    "belgian": "Belgian",
    "brasseries": "Brasseries",
    "brazillian": "Brazillan",
    "breakfast_brunch": "Breakfast/Brunch",
    "british": "British",
    "buffets": "Buffets",
    "burgers": "Burgers",
    "burmese": "Burmese",
    "cajun": "Cajun",
    "cambodian": "Cambodian",
    "caribbean": "Caribbean",
    "cheesesteaks": "Cheesesteak",
    "chinese": "Chinese",
    "dimsum": "Dim Sum",
    "creperies": "Creperies",
    "cuban": "Cuban", "delis":
    "Delis", "diners": "Diners",
    "etheopian": "Etheopian",
    "hotdogs": "Fast Food",
    "filipino": "Filipino",
    "fishnchips": "Fish and Chips",
    "fondue": "Fondue",
    "foodstands": "Foodstands",
    "french": "French",
    "gastropub": "Gastro Pub",
    "german": "German", "greek":
    "Greek", "halal": "Halal",
    "hawaiian": "Hawaiian",
    "himalayan": "Himalayan",
    "hotdog": "Hot Dogs",
    "hungarian": "Hungarian",
    "indpak": "Indian Pakistani",
    "indonesian": "Indonesian",
    "irish": "Irish",
    "italian": "Italian",
    "japanese": "Japanese",
    "korean": "Korean",
    "latin": "Latin",
    "malaysian": "Malaysian",
    "mediterranean": "Mediterranean",
    "mexican": "Mexican",
    "mideastern": "Middle Eastern",
    "modern_european": "Modern European",
    "mongolian": "Mongolian",
    "moroccan": "Moroccan",
    "pakistani": "Pakistani",
    "persian": "Persian",
    "peruvian": "Peruvian",
    "pizza": "Pizza",
    "polish": "Polish",
    "portuguese": "Portuguese",
    "russian": "Russian",
    "sandwiches": "Sandwiches",
    "scandinavian": "Scandinavian",
    "seafood": "Seafood",
    "singaporean": "Singaporean",
    "soulfood": "Soul Food",
    "soup": "Soup",
    "southern": "Southern",
    "spanish": "Spanish",
    "steak": "Steak",
    "sushi": "Sushi",
    "taiwanese": "Taiwanese",
    "tapas": "Tapas",
    "tapasmallplates": "Tapas (Small Plates)",
    "tex-mex": "Tex-Mex",
    "thai": "Thai",
    "turkish": "Turkish",
    "ukrainian": "Ukranian",
    "vegan": "Vegan",
    "vietnamese": "Vietnamese",
}


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
