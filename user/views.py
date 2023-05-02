from rest_framework import generics

from .models import User
from .serializers import UserRegisterSerializers


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializers
