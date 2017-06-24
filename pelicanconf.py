#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = 'content'

# Personalized by Andrew
USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
AUTHOR = 'Andrew Li'
SITENAME = "Andrew's Blog"
SITEURL = 'http://blog.lishuchen.com'

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'EN'
DEFAULT_DATE_FORMAT = '%a, %b %d %Y'
LOCALE = ('usa',      # On Windows
           'en_US',   # On Unix/Linux
)
OUTPUT_RETENTION = ['.git']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
         # ('Python.org', 'http://python.org/'),
         # ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/lishuchen'),
		  ('rss', SITEURL + '/feeds/all.atom.xml'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Settings for "Flex"
THEME = "../themes/flex"
FAVICON = SITEURL + '/images/favicon.ico'
SITELOGO = SITEURL + '/images/avatar.png'

STATIC_PATHS = ['images', 'extra', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

SITETITLE = AUTHOR
SITESUBTITLE = 'Life is short, use Python'
#SITEDESCRIPTION = 'Life is short, use Python'

import datetime
COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = datetime.datetime.now().year

MAIN_MENU = True
HOME_HIDE_TAGS = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
			 ('Sitemap', '/sitemap.xml'))

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["sitemap", "gzip_cache", "neighbors", "related_posts", "optimize_images"]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}