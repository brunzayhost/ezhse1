from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    
    # User management
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Local apps
    path('', include('pages.urls')),
]
