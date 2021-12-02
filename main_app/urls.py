from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', views.Feed.as_view(), name='feed'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('entry/create/', views.EntryCreate.as_view(), name ='entry_create'),
    path('entry/<int:pk>/', views.detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('entry/<int:pk>/update/', views.EntryUpdate.as_view(), name='entry_update'),
    path('entry/<int:pk>/delete/', views.EntryDelete.as_view(), name='entry_delete'),
    path('tags/<slug:tags_slug>/', views.TagIndexView.as_view(), name='posts_by_tag'),
    path('entry/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
   
]