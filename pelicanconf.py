#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'LCY'
SITENAME = u'LCY Data Science Couple'
SITETITLE = u'LCY Data Science Couple'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['theme/images', 'images']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'zh'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

# Theme
#THEME = "themes/pelican-bootstrap3"
THEME = "themes/pelican-elegant"

# About us
LANDING_PAGE_ABOUT = dict()
#LANDING_PAGE_ABOUT['title'] = 'Test'
LANDING_PAGE_ABOUT['details'] = 'Welcome to our tiny site :-) \r\n 我们是'

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["render_math", "representative_image", "ipynb"]

MARKUP = ('md', 'ipynb')

# Pics on the pages
BANNER = 'images/LCYbanner_1500.png'
BANNER_ALL_PAGES = True
SITELOGO = 'images/white.png'
HIDE_SITENAME = True

# Config of elegant
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

PROJECTS = [
	{'name': 'ROC4ML',
    'url': 'https://github.com/lcy-hugepanda/ROC4ML',
    'description': 'A simple ROC (Receiver Operating Characteristic) analysis '
    'and visualization tool for machine learning algorithms.'},
    {'name': 'MLAlgoTester',
    'url': 'https://github.com/lcy-hugepanda/MLAlgoTester',
    'description': 'An automatic evaluating framework for machine learning algorithms'},
	{'name': 'LCY-ML-Demos',
    'url': 'https://github.com/lcy-hugepanda/LCY-ML-Demos',
    'description': 'Some interesting (and useful :) ) demos of machine learning algorithms'}]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
