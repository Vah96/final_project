from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .utils import guest_user

app_name = 'auth'
urlpatterns = [
    path('register/', guest_user(views.register, 'You have already registered'), name='register'),
    path('login/', guest_user(auth_views.LoginView.as_view(), 'You have already signed'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
