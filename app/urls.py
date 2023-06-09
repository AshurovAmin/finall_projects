from django.urls import path, include
from rest_framework import routers

from . import views

urlpatterns = [
    path('event/', views.EventListAPIView.as_view()),
    path('event/create/', views.EventCreateAPIView.as_view()),
    path('event/<int:pk>/', views.EventUpdateDestroyAPIView.as_view()),
    path('event/<int:pk>/detail/', views.EventRetrieveAPIView.as_view()),
    path('profile/create/', views.ProfileCreateAPIView.as_view()),
    path('profile/<str:user__username>/', views.ProfileUpdateRetrieveDestroyAPIView.as_view()),

]