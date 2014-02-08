"""Settings for Development Server"""
from homesoko.settings.custom import *  # pylint: disable=W0614,W0401 @UnusedWildImport

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = {
    '127.0.0.1',
    'localhost',
}

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

import sys
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(PROJECT_DIR, 'dev.db'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'homesoko',  # Or path to database file if using sqlite3.
            'USER': 'root',  # Not used with sqlite3.
            'PASSWORD': 'serviola',  # Not used with sqlite3.
            'HOST': 'localhost',  # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
            'OPTIONS': {"init_command": "SET storage_engine=INNODB"}
        }
    }

# Turn warnings about naive datetime into errors
import warnings
warnings.filterwarnings('error', r"DateTimeField received a naive datetime",
                        RuntimeWarning, r'django\.db\.models\.fields')
