# Custom application settings - anything that's not required by core Django
from homesoko.settings.base import *  # pylint: disable=W0614,W0401 @UnusedWildImport

#=============================
# Version number
#============================
VERSION = '0.1'

# static and media files
import homesoko as project_module
PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'custom-static'),
    os.path.join(PROJECT_DIR, 'frontend-static'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)
###########################################
# django-userena settings
###########################################
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)
ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'users.Profile'
USERENA_MUGSHOT_GRAVATAR = False
USERENA_SIGNIN_REDIRECT_URL = '/dashboard/properties'
LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

##################################################################
# Haystack settings
##################################################################
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}
