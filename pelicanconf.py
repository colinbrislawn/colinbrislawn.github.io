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

# Blogroll
LINKS = (
	('Works at PNNL', 'http://www.pnnl.gov/biology/staff/staff_info.asp?staff_num=8191'),
	('Alum of Lamendella Labs', 'http://jcsites.juniata.edu/faculty/lamendella/'),
	('Alum of Juniata College', 'www.juniata.edu'),
	)

# Social widget
SOCIAL = (
	('GitHub', 'https://github.com/colinbrislawn'),
	('Linkedin', 'https://www.linkedin.com/pub/colin-brislawn/a3/233/7'),
	('Google Scholar', 'https://scholar.google.com/citations?user=fyhedCwAAAAJ&hl=en'),
	('ORCID', 'https://orcid.org/0000-0002-9109-1950'),
	# ('Not on Facebook', 'https://www.facebook.com/pages/King-Colin-Brislawn/216922768365881'),
	)

DEFAULT_PAGINATION = 5

STATIC_PATHS = ['images', 'pages', 'extra/CNAME']

# THEME = '../pelican-themes/simple-bootstrap'
# THEME = '../CamerataMusica/pelican-bootstrap3' # works, lol
THEME = 'theme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True