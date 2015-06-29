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
	('Works at PNNL', 'http://www.pnnl.gov/biology/staff/staff_info.asp?staff_num=8191'),
	('Alum of Lamendella Labs', 'http://jcsites.juniata.edu/faculty/lamendella/'),
	('Alum of Juniata College', 'www.juniata.edu'),
	)

# Social widget
SOCIAL = (
	('GitHub', 'https://github.com/colinbrislawn'),
	('Google+', 'https://plus.google.com/+ColinBrislawn'),
	('Linkedin', 'https://www.linkedin.com/pub/colin-brislawn/a3/233/7'),
	('Not on Facebook', 'https://www.facebook.com/pages/King-Colin-Brislawn/216922768365881'),
	)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = "../pelican-themes/pelican-bootstrap3"

PLUGIN_PATHS = ['../pelican-plugins']
#PLUGINS=['sitemap',]
