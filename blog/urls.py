from django.urls import path

from .views import create_post, get_post, update_post

urlpatterns = [
    path('posts/<int:pk>/update', update_post, name='posts-update'),
    path('posts/<int:pk>', get_post, name='posts-get'),
    path('posts/', create_post, name='posts-create'),
]
