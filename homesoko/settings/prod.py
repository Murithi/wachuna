
from homesoko.settings.custom import *  # pylint: disable=W0614,W0401 @UnusedWildImport

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (('Eric Murithi', 'ericinoti@gmail.com'),)

# ALLOWED_HOSTS = {
#     '127.0.0.1',
#     'www.homesoko.com',
#     'homesoko.com',
# }
ALLOWED_HOSTS= {'*'}
#==============================================================================
# Database
#==============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'homesoko',  # Or path to database file if using sqlite3.
        'USER': 'root',  # Not used with sqlite3.
        'PASSWORD': 'root',  # Not used with sqlite3.
        'HOST': 'localhost',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {"init_command": "SET storage_engine=INNODB"}
    }
}


#==============================================================================
# Email Settings
#==============================================================================
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'mspropertiesmail@gmail.com'
EMAIL_HOST_PASSWORD = 'msproperties'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

#==============================================================================
# Logging
#==============================================================================
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
