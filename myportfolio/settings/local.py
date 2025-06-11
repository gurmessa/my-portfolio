# myportfolio/settings/local.py
from .base import *

# Allow any host during local development
ALLOWED_HOSTS = ["*"]

# Use SQLite for local development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db/db.sqlite3",
    }
}


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = '/static/'