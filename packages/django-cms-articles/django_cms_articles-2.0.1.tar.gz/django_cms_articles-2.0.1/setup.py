# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cms_articles',
 'cms_articles.admin',
 'cms_articles.conf',
 'cms_articles.import_wordpress',
 'cms_articles.import_wordpress.management',
 'cms_articles.import_wordpress.management.commands',
 'cms_articles.import_wordpress.migrations',
 'cms_articles.migrations',
 'cms_articles.models',
 'cms_articles.signals',
 'cms_articles.templatetags',
 'cms_articles.tests',
 'cms_articles.utils']

package_data = \
{'': ['*'],
 'cms_articles': ['locale/cs/LC_MESSAGES/*',
                  'static/cms_articles/css/*',
                  'static/cms_articles/js/*',
                  'templates/admin/cms_articles/*',
                  'templates/admin/cms_articles/article/*',
                  'templates/cms_articles/*',
                  'templates/cms_articles/article/*',
                  'templates/cms_articles/articles/*'],
 'cms_articles.import_wordpress': ['templates/cms_articles/import_wordpress/*'],
 'cms_articles.tests': ['templates/*']}

install_requires = \
['Django<4',
 'django-cms<3.12',
 'django-filer',
 'djangocms-text-ckeditor',
 'python-dateutil']

setup_kwargs = {
    'name': 'django-cms-articles',
    'version': '2.0.1',
    'description': 'django CMS application for managing articles',
    'long_description': '# django-cms-articles\nthe best django CMS application for managing articles\n\nThis application provides full featured articles management for django CMS.\nIt is heavily inspired by (and partially copied from) the page management in django CMS itself.\n\n## Features\n\n * intuitive admin UI inspired by django CMS page UI\n * intuitive front-end editing using placeholders and toolbar menu\n * supports multiple languages (the same way as django CMS does)\n * publisher workflow from django CMS\n * flexible plugins to render article outside django CMS page\n\n## Installation and usage\n\nInstallation and usage is quite traightforward.\n * install (using pip) django-cms-articles\n * add "cms_articles" into your settings.INSTALLED_APPS\n * check cms_articles.conf.default_settings for values you may want to override in your settings\n * add "Articles Category" apphook to any django CMS page, which should act as category for articles\n * add "Articles" plugin to placeholder of your choice to show articles belonging to that page / category\n\n## Bugs and Feature requests\n\nShould you encounter any bug or have some feature request,\ncreate an issue at https://github.com/misli/django-cms-articles/issues.\n',
    'author': 'Jakub Dorňák',
    'author_email': 'jakub.dornak@qbsoftware.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/misli/django-cms-articles',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
