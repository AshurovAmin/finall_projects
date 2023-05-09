from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.db.utils import IntegrityError

from .models import Event, Profile, User


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['user', ]


class ProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ['user', ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError('Профиль данного пользователя уже существует!')
