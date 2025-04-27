from django.urls import path
from .views import RegisterUser, LoginUser, ListUser, UpdateUser, DeleteUser


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('list_user/', ListUser.as_view(), name='list_user'),
    path('update_user/<int:pk>/', UpdateUser.as_view(), name='update_user'),
    path('delete_user/<int:pk>/', DeleteUser.as_view(), name='delete_user'),
]
