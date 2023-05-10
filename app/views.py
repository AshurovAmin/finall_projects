from rest_framework import viewsets, mixins, generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissons import IsAuthorOrAllowAny
from .models import Event, Profile
from .serializers import EventSerializers, ProfileSerializers


class EventListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EventUpdateDestroyAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthorOrAllowAny, ]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class EventCreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventRetrieveAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthorOrAllowAny, ]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProfileCreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthorOrAllowAny, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProfileUpdateRetrieveDestroyAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthorOrAllowAny, ]
    lookup_field = 'user__username'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

