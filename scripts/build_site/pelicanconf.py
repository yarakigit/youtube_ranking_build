AUTHOR = 'youtube ranking'
SITENAME = 'youtube ranking'
SITEURL = 'https://yarakigit.github.io/youtube_ranking_build/'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# my setting
THEME = './flex'

DATE_FORMATS = {
    'ja': '%Y-%m-%d',
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.fenced_code': {},
        'markdown.extensions.nl2br': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.admonition': {},
        'mdx_linkify.mdx_linkify': {},
    },
    'output_format': 'html5',
}

MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
)

