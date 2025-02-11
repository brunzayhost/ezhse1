from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # django admin
    path("admin/", admin.site.urls),
    # user management
    path("accounts/", include("allauth.urls")),  # Include allauth URLs
    # local app
    path("", include("pages.urls")),  # Include pages URLs
]
