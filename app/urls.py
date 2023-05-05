from django.urls import path, include
from rest_framework import routers

from . import views

urlpatterns = [
    path('event/', views.EventListAPIView.as_view()),
    path('event/create/', views.EventCreateAPIView.as_view()),
    path('event/<int:pk>/', views.EventUpdateDestroyAPIView.as_view()),
    path('profile/', views.ProfileViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}
    )),

]