from .base import *


TEMPLATES[0]['DIRS'].append(os.path.join(BASE_DIR, 'templates'))

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
