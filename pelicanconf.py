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
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/acrdijon'),
          ('envelope', 'mailto:contact@acr-dijon.org'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/mg'

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search',
                    'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'
FAVICON = 'favicon.ico'
FAVICON_TYPE = 'image/vnd.microsoft.icon'

FOOTER = "&copy; 2015 ACR Dijon. Tout droits réservés."

SHARE = True
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
