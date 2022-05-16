from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AphorismListView, AphorismCreateView, AphorismUpdateView, AphorismDeleteView

app = 'aphorisms'
urlpatterns = [
    path('user_aphorisms/<int:user_id>', AphorismListView.as_view(), name='user_aphorism_list'),
    path('aphorisms/create', login_required(AphorismCreateView.as_view()), name='create'),
    path('aphorisms/create/<int:pk>', login_required(AphorismUpdateView.as_view()), name='update'),
    path('aphorisms/delete/<int:pk>', login_required(AphorismDeleteView.as_view()), name='delete'),
    path('', AphorismListView.as_view(), name='aphorism_list'),
]
