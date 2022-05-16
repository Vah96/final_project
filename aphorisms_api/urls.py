from django.urls import path, include
from rest_framework import routers
# from .views import AphorismListViewSet
import aphorisms_api.views as views

# router = routers.DefaultRouter()
# router.register(r'api/aphorisms', views.tutorial_list, basename='home')
# router.register(r'^api/aphorisms', AphorismListViewSet),

app_name = 'aphorisms_api'
urlpatterns = [

    path(r'api/aphorisms', views.aphorism_list),
    path(r'api/aphorisms/<int:pk>', views.aphorism_detail),
    # path('', include(router.urls))
]
