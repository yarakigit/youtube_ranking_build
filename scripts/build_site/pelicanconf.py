EN_GITHUB_PAGES = True
if EN_GITHUB_PAGES:
    root_dir = '/youtube_ranking_build'
AUTHOR = 'youtube ranking'
SITEURL = 'https://yarakigit.github.io/youtube_ranking_build/'
SITENAME = 'youtube ranking'
SITETITLE = "youtube ranking"
#SITESUBTITLE = "The minimalist Pelican theme"
#SITEDESCRIPTION = "Flex - The minimalist Pelican theme."
# SITELOGO = ''
# FAVICON = '/images/favicon.ico'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"
ROBOTS = "index, follow"

# my setting
THEME = "./flex"
PATH = 'content'
#OUTPUT_PATH = "blog/"
TIMEZONE = 'Asia/Tokyo'

DISABLE_URL_HASH = True

# PLUGIN_PATHS = ['pelican-plugins']

# PLUGINS = ['i18n_subsites']

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

#I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "ja"
#OG_LOCALE = "en_US"
#LOCALE = "en_US"

DATE_FORMATS = {
    'ja': '%Y-%m-%d',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

#SOCIAL = (
#    ("github", "https://github.com/alexandrevicenzi/Flex"),
#    ("rss", "/blog/feeds/all.atom.xml"),
#)

if EN_GITHUB_PAGES:
    MENUITEMS = (
        ("Archives", root_dir+"/archives.html"),
        ("Categories", root_dir+"/categories.html"),
        ("Tags", root_dir+"/tags.html"),
    )
else:
    MENUITEMS = (
        ("Archives", "/archives.html"),
        ("Categories", "/categories.html"),
        ("Tags", "/tags.html"),
    )

#CC_LICENSE = {
#    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
#    "version": "4.0",
#    "slug": "by-sa",
#    "icon": True,
#    "language": "en_US",
#}

#COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 7

#DISQUS_SITENAME = "flex-pelican"
#ADD_THIS_ID = "ra-55adbb025d4f7e55"

#STATIC_PATHS = ["images", "extra/ads.txt", "extra/CNAME"]

#EXTRA_PATH_METADATA = {
#    "extra/ads.txt": {"path": "ads.txt"},
#    "extra/CNAME": {"path": "CNAME"},
#}

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

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
