from django.contrib import admin
from django.urls import path
from pages.views import HomePageView  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),  # Add this line
]
