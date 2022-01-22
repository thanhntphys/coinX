from django.urls import path
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    CreatPostAPIView
)

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', CreatPostAPIView.as_view(), name='post-create'),
    path('<str:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
]
