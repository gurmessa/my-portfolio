# myportfolio/settings/production.py
from .base import *
import os

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# PostgreSQL Example
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db/db.sqlite3",
    }
}

# HTTPS & Security Settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = '/static/'

CSRF_TRUSTED_ORIGINS=env.list("CSRF_TRUSTED_ORIGINS")
