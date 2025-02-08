from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  # Include accounts URLs
    path("", include("pages.urls")),  # Include pages URLs
]
