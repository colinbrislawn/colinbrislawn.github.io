#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colin Brislawn'
SITENAME = u'Colin Brislawn'
SITEURL = 'http://colinbrislawn.github.io'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Not on Facebook', 'https://www.facebook.com/pages/King-Colin-Brislawn/216922768365881'),
    ('Works at PNNL', 'http://www.pnnl.gov/biology/staff/staff_info.asp?staff_num=8191'),
    ('Made with Pelican', 'http://getpelican.com/'),
    )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = "../pelican-themes/pelican-bootstrap3"

PLUGIN_PATHS = ['../pelican-plugins']
#PLUGINS=['sitemap',]
