# accounts/urls.py
from django.urls import path
from .views import SignupPageView
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.SignupPageView.as_view(), name='signup'),
]