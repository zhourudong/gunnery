from __future__ import absolute_import
from .common import *
ENVIRONMENT = 'development'

DEBUG = True

TEMPLATE_DEBUG = True

import uuid
uuid._uuid_generate_random = None

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

from fnmatch import fnmatch


class glob_list(list):
    def __contains__(self, key):
        for elt in self:
            if fnmatch(key, elt): return True
        return False


INTERNAL_IPS = glob_list(['127.0.0.1', '10.0.*.*'])

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_PATCH_SETTINGS = False
