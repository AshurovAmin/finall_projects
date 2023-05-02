from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Category, Event, EventGroup
from .serializers import CategorySerializers, EventSerializers, EventGroupSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializers
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = EventGroup.objects.all()
    serializer_class = EventGroupSerializers
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]