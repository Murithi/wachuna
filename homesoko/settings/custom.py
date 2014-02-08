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
IMAGE_FOLDER = os.path.join(PROJECT_DIR, 'media/images')

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'custom-static'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

