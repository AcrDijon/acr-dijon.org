#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Equipe ACR'
ALT_NAME = SITENAME = u'Association des Coureurs sur Route de Dijon'
SITEURL = 'http://localhost:8000'
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Athle.fr', 'http://www.athle.fr/ffa.performance/'),
        ('Ligue Bourgogne', 'http://ffaliguebou.pagesperso-orange.fr/'),
        ("J'aime Courir", 'http://www.jaimecourir.fr/'),
        ('CDCHS 21', 'http://www.cdchs21.fr'),
        ('Challenge Etoile', 'http://www.everyoneweb.fr/challengeetoile21')
)

# Social widget
SOCIAL = [('envelope', 'mailto:contact@acr-dijon.org')]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/mg'

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'search', 'tipue_search')
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'
FAVICON = 'favicon.ico'
FAVICON_TYPE = 'image/vnd.microsoft.icon'

FOOTER = "&copy; 2015 ACR Dijon. Tout droits réservés."

SHARE = False
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

TWITTER_USERNAME = 'acrdijon'
DISQUS_SITENAME = "httpacrziadeorg"
SC_PROJECT = '10431657'
SC_SECURITY = 'fb0b78b3'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'

from pelican.utils import strftime, get_date


def str2defaultformat(data):
    return strftime(get_date(data), DEFAULT_DATE_FORMAT)


JINJA_FILTERS = {'str2defaultformat': str2defaultformat}
