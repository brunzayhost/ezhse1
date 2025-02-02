from django.contrib import admin
from django.urls import path
from pages.views import home_page_view  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name='home'),  # Add this line
]
