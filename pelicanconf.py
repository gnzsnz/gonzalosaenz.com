#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gonzalo Saenz'
SITENAME = 'Gonzalo Saenz'
SITEURL = 'https://gonzalosaenz.com'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
#LINKS = (('Text', 'http://text.com'),
        #('Python.org', 'http://python.org/'),
        #)
# to publish change article status to Status: published
DEFAULT_METADATA = {
    'Status': 'draft',
}

THEME = 'themes/theme-gonzalosaenz.com'
#THEME = '/Users/gonzo/Documents/dev/pelican-themes/theme-gonzalosaenz.com'
#STATIC_PATHS = ['img', 'static']
#FAVICON = 'img/favicon.ico'
STATIC_PATHS = ['images']


# Social widget
SOCIAL = (('Gonzalo Saenz on LinkedIn', 'https://www.linkedin.com/in/gonzalosaenzdequiroz/'),
        ('Follow me @gnzsnz', 'https://twitter.com/gnzsnz'),)

TWITTER_USERNAME='gnzsnz'

DEFAULT_PAGINATION = 10

SCHNACK = "http://osvaldo.local:3000/embed.js"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
