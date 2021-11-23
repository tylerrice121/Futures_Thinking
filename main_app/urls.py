from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', views.Feed.as_view(), name='feed'),
    path('profile/', views.Profile.as_view(), name='profile')
]