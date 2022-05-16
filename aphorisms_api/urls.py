from django.urls import path, include
from rest_framework import routers
import aphorisms_api.views as views


app_name = 'aphorisms_api'
urlpatterns = [
    path(r'api/get-aphorisms', views.get_aphorism_list),
    path(r'api/aphorisms', views.aphorism_list),
    path(r'api/aphorisms/<int:pk>', views.aphorism_detail),
]
