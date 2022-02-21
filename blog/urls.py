from django.urls import path

from .views import create_post

urlpatterns = [
    path('posts/', create_post, name='posts-create'),
]
