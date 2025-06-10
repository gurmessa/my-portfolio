"""
WSGI config for myportfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import environ
from django.core.wsgi import get_wsgi_application

environ.Env().read_env()

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", os.environ.get("DJANGO_SETTINGS_MODULE", "myportfolio.settings.production")
)


application = get_wsgi_application()
