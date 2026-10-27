import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://www.loughdergrally50.com'
RELATIVE_URLS = False

# Only build the standalone announcements splash page, no archive or articles
ARTICLE_PATHS = []
PAGE_PATHS = ['pages/announcements.md']

# Make announcements.md render directly as the root homepage (index.html)
EXTRA_PATH_METADATA = {
    'pages/announcements.md': {
        'save_as': 'index.html',
        'url': '',
    },
}

# Only copy theme assets (no need to copy the entire archive of images/audio to the public repo)
STATIC_PATHS = []

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
DELETE_OUTPUT_DIRECTORY = True
