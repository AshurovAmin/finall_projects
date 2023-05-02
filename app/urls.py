from django.urls import path, include
from rest_framework import routers

from . import views
routers = routers.DefaultRouter()
routers.register('category', views.CategoryViewSet)
routers.register('event', views.EventViewSet)
routers.register('group', views.GroupViewSet)

urlpatterns = [
    path('', include(routers.urls)),

]