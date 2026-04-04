from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("terms-of-service/", views.terms_of_service, name="terms_of_service"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
]