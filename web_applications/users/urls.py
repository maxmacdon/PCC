"""Defines URL patterns for users"""

from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    # Login page.
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Logout page.
    path('logout/', views.logout_view, name='logout'),
    # Registration page.
    path('register/', views.register, name='register'),
]