from django.urls import path
from .views import RegisterUser, LoginUser, ListUser


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('list_user/', ListUser.as_view(), name='list_user'),
]