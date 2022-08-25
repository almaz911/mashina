from main import views
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *


# router = SimpleRouter()
# router.register('image', PostImageView)
urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='categories-list'),
    path('posts/', views.PostView.as_view(), name='posts-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/update/<int:pk>/', views.PostUpdateView.as_view()),
    path('posts/delete/<int:pk>/', views.PostDeleteView.as_view()),
    # path('post/', views.PostImageView.as_view()),
    # path('', include(router.urls)),
]