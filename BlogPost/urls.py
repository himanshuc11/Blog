from django.urls import path
from .views import AllPostAPIView, UserPostListAPIView, CreateAPIView, UpdateAPIView

urlpatterns = [
    path('', AllPostAPIView.as_view(), name="post"),
    path('<int:id>/', UserPostListAPIView.as_view(), name="user's_posts"),
    path('create/', CreateAPIView.as_view(), name="create"),
    path('edit/<int:id>/', UpdateAPIView.as_view(), name="update")
]
