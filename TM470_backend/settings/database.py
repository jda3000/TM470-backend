import os
from .django import DEBUG, BASE_DIR
from decouple import config

from dj_database_url import parse as dburl

DEFAULT_DBURL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
print('debug', DEBUG)
if DEBUG:
    print('here 1')
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'tm470',
            'USER': 'jamesalexander',
            'PASSWORD': 'mypassword',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
else:
    print('here 2')
    DATABASES = {
        'default': config('PRODUCTION_DB_URL', default=DEFAULT_DBURL, cast=dburl)
    }
