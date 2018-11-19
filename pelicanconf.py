#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from __future__ import absolute_import
from docutils import nodes
from docutils.parsers.rst import Directive, directives
import time


def align(argument):
    """Conversion function for the "align" option."""
    return directives.choice(argument, ('left', 'center', 'right'))


def key(argument):
    return argument


class OpenRunner(Directive):

    html = ('<script type="text/javascript" src="http://www.openrunner.com/orservice/inorser-script.php?'
            'key=%(key)s&amp;ser=S08&amp;id=%(run_id)s&amp;w=%(width)s&amp;'
            'h=%(height)s&amp;k=5&amp;m=0&amp;ts=%(timestamp)s"></script>')
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'height': directives.nonnegative_int,
        'width': directives.nonnegative_int,
        'key': key,
        'align': align
    }
    default_width = 750
    default_height = 500
    default_key = 'mykey'

    def run(self):
        self.options['run_id'] = directives.uri(self.arguments[0])
        if not self.options.get('key'):
            self.options['key'] = self.default_key
        if not self.options.get('width'):
            self.options['width'] = self.default_width
        if not self.options.get('height'):
            self.options['height'] = self.default_height
        if not self.options.get('align'):
            self.options['align'] = 'left'
        self.options['timestamp'] = '1459857519'

        return [nodes.raw('', self.html % self.options, format='html')]


class IframeVideo(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'height': directives.nonnegative_int,
        'width': directives.nonnegative_int,
        'align': align,
    }
    default_width = 500
    default_height = 281

    def run(self):
        self.options['video_id'] = directives.uri(self.arguments[0])
        if not self.options.get('width'):
            self.options['width'] = self.default_width
        if not self.options.get('height'):
            self.options['height'] = self.default_height
        if not self.options.get('align'):
            self.options['align'] = 'left'
        return [nodes.raw('', self.html % self.options, format='html')]


class Youtube(IframeVideo):
    html = '<iframe src="http://www.youtube.com/embed/%(video_id)s" \
    width="%(width)u" height="%(height)u" frameborder="0" \
    webkitAllowFullScreen mozallowfullscreen allowfullscreen \
    class="youtube align-%(align)s"></iframe>'


class Vimeo(IframeVideo):
    html = '<iframe src="http://player.vimeo.com/video/%(video_id)s" \
    width="%(width)u" height="%(height)u" frameborder="0" \
    webkitAllowFullScreen mozallowfullscreen allowFullScreen \
    class="youtube align-%(align)s"></iframe>'


directives.register_directive('youtube', Youtube)
directives.register_directive('vimeo', Vimeo)
directives.register_directive('openrunner', OpenRunner)

AUTHOR = u'Equipe ACR'
ALT_NAME = SITENAME = u'Association des Coureurs sur Route de Dijon'
SITEURL = 'http://localhost:8000'
PATH = u'content'
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
        ('Challenge Etoile', 'http://challenge-etoile21.com'),
        ("Bulletin d'inscription", "https://assets.acr-dijon.org/bulletin2018-2019.pdf")
)

# Social widget
SOCIAL = [('envelope', 'mailto:acr.dijon@gmail.com')]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/mg'

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'search', 'tipue_search')
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'
FAVICON = 'theme/favicon.ico'
FAVICON_TYPE = 'image/vnd.microsoft.icon'

FOOTER = "&copy; 2016 ACR Dijon. Tout droits réservés."

SHARE = False
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

TWITTER_USERNAME = 'acrdijon'
#DISQUS_SITENAME = "httpacrziadeorg"
SC_PROJECT = '10431657'
SC_SECURITY = 'fb0b78b3'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'

from pelican.utils import strftime, get_date


def str2defaultformat(data):
    return strftime(get_date(data), DEFAULT_DATE_FORMAT)


JINJA_FILTERS = {'str2defaultformat': str2defaultformat}

ISSO_SERVER = "http://localhost:9999"
