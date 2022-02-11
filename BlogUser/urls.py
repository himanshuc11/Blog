from django.urls import path
from .views import UserLoginAPIView, UserLogoutView, RegistrationAPIView, ListUserAPIView, UserDetailAPIView

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('registration/', RegistrationAPIView.as_view(), name="registration"),
    path('list/', ListUserAPIView.as_view(), name="list"),
    path('detail/<int:id>/', UserDetailAPIView.as_view(), name="detail")
]
