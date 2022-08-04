AUTHOR = 'Colin Brislawn'
SITENAME = 'Colin Brislawn'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_ARCHIVES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = False # for now, as I have no tags

# Social widget
SOCIAL = (
	('GitHub', 'https://github.com/colinbrislawn'),
	('Linkedin', 'https://www.linkedin.com/pub/colin-brislawn/a3/233/7'),
	('Google Scholar', 'https://scholar.google.com/citations?user=fyhedCwAAAAJ&hl=en'),
	('ORCID', 'https://orcid.org/0000-0002-9109-1950')
	)

# Blogroll
LINKS = (
	('Staff Scientist at PNNL', 'https://biology.pnnl.gov/people/colin-brislawn'),
	('Director of Computational Informatics at CSI', 'https://csidx.com'),
	('PI: Regina Lamendella', 'https://en.wikipedia.org/wiki/Regina_Lamendella'),
	('PI: Janet Jansson', 'https://www.pnnl.gov/people/janet-jansson'),
	('PI: Hans Bernstein', 'https://twitter.com/microbe_angler?lang=en'),
	)

DEFAULT_PAGINATION = 5

STATIC_PATHS = ['images', 'pages'] #, 'extra/CNAME']

THEME = 'theme' # local copy of pelican-bootstrap3
# THEME = '../pelican-themes/built-texts' # pretty good!

# THEME = '../pelican-themes/html5-dopetrope' # Needs edits to footer, body images
# THEME = '../pelican-themes/brutalist' # very clean, missing lots
# THEME = '../pelican-themes/Flex' # very clean, responsive, needs edits to sidebar and menu
# THEME = '../pelican-themes/gum' # very clean, almost ready to go
# THEME = '../pelican-themes/MinimalXY' # very clean, commercial, everything is pages
# THEME = '../pelican-themes/nest' # great image header, missing menu, needs work
# THEME = '../pelican-themes/resume' # needs configuration, single page


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Settings for html5-dopetrope
MAIL = "cbrisl@gmail.com"
LINKEDIN_USER  = "007233a3"
# ABOUT_TEXT = "Testing where this goes"