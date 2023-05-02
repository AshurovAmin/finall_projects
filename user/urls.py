from django.urls import path
from rest_framework.authtoken import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view()),
    path('login/', views.UserList.as_view()),
    path('auth_token/', auth_views.obtain_auth_token),

]
