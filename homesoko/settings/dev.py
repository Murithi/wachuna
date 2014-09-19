"""Settings for Development Server"""
from homesoko.settings.custom import *  # pylint: disable=W0614,W0401 @UnusedWildImport

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = {
    '127.0.0.1',
    'localhost',
}


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
            'USER': 'flor',  # Not used with sqlite3.
            'PASSWORD': '}3;)4.06J95qS2A',  # Not used with sqlite3.
            'HOST': 'localhost',  # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
            'OPTIONS': {"init_command": "SET storage_engine=INNODB"}
        }
    }

# Testing
SOUTH_TESTS_MIGRATE = False  # To disable migrations and use syncdb instead
SKIP_SOUTH_TESTS = True  # To disable South's own unit tests

# Django Nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
DDF_FILL_NULLABLE_FIELDS = False
DDF_USE_LIBRARY = True

# Turn warnings about naive datetime into errors
import warnings
warnings.filterwarnings('error', r"DateTimeField received a naive datetime",
                        RuntimeWarning, r'django\.db\.models\.fields')

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


