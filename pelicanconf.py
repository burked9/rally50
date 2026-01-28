AUTHOR = 'Rally 50 Committee'
SITENAME = 'IWAI Lough Derg Rally 50'
SITEURL = ''

PATH = 'content'

ARTICLE_PATHS = ['articles', 'announcements']
PAGE_PATHS = ['pages', 'archive']

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Navigation
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Home', '/'),
    ('About', '/pages/about.html'),
    ('Archive', '/pages/archive.html'),
    ('Articles', '/category/articles.html'),
    ('Announcements', '/category/announcements.html'),
    ('Photos', '/pages/photos.html'),
)

# Theme
THEME = 'theme'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static paths
STATIC_PATHS = ['images', 'js', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
