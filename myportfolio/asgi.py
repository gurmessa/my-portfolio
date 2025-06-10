"""
ASGI config for myportfolio project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import environ
from django.core.asgi import get_asgi_application

# Load env
environ.Env().read_env()

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", os.environ.get("DJANGO_SETTINGS_MODULE", "myportfolio.settings.production")
)

application = get_asgi_application()
