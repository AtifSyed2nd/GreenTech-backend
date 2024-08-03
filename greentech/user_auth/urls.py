from django.urls import path
from .views import GetUserListView,RegisterView,LoginView,GetUserView

urlpatterns = [
    path('get-user-list',GetUserListView.as_view(),name='get-users'),
    path('user/<str:pk>',GetUserView.as_view(),name='get-user'),
    path('register/nt/',RegisterView.as_view(),name='register'),
    path('login/nt/',LoginView.as_view(),name='login'),
]

# {
# "username": "test",
# "email":"test@gmail.com",
# "password":"test123"
# }