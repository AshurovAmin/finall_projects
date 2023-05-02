from rest_framework import serializers

from .models import User


class UserRegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def create(self, validated_data):
        user = User(
            username=validated_data.get('username'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user