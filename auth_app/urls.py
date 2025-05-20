from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterUser, LoginUser, ListUser, UpdateUser, DeleteUser


urlpatterns = [
    # Cadastro users
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('list_user/', ListUser.as_view(), name='list_user'),
    path('update_user/<int:pk>/', UpdateUser.as_view(), name='update_user'),
    path('delete_user/<int:pk>/', DeleteUser.as_view(), name='delete_user'),
    # JWT endpoints:
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
