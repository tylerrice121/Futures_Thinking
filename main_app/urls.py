from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', views.feed, name='feed'),
    path('profile/', views.Profile.as_view(), name='profile')
]