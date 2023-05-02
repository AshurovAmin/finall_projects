from rest_framework import generics

from .models import User
from .serializers import UserRegisterSerializers, UserSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializers


class UserList(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

