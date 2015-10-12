#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'LCY'
SITENAME = u'LCY Data Science Couple'
SITETITLE = u'LCY Data Science Couple'
SITEURL = ''
DISQUS_URL = "lcy-couple.disqus.com"
SITESUBTITLE = 'Welcome :-)'

PATH = 'content'
# STATIC_PATHS = ['theme/images', 'images']

TIMEZONE = 'Asia/Chongqing'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None		 

# Theme
#THEME = "themes/pelican-bootstrap3"
# THEME = "themes/pelican-elegant"
THEME = "themes/backdrop"

# Theme parameters
# --> color modification in 'backdrop.css':
#	#71030C --> #005732 (top-bar)
#	#a21723 --> #007D47 (other)
# DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives'))
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 5
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')
PROFILE_IMAGE = "images/LCYlogo_Baidu.png"
BACKDROP_IMAGE = 'images/background.jpg'
SITE_DESCRIPTION = '我们是LCY Data Science Couple，热爱数据科学和相关技术，欢迎来到我们的小站，有任何问题可以直接联系我们。我们的新浪微博是 @居里猴弟 和 @居里猴姐。'
SOCIAL=[('Weibo','http://weibo.com/u/1706903234'),
		('Weibo','http://weibo.com/lcyseso'),
        ('GitHub','https://github.com/lcy-hugepanda')]
EMAIL='lcycouple@gmail.com'

# Plugins
PLUGIN_PATHS = ["plugins"]
# PLUGINS = ["render_math", "representative_image", "ipynb"]
PLUGINS = ["render_math", "representative_image"]

# MARKUP = ('md', 'ipynb')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
