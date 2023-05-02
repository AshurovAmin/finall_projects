from rest_framework import serializers

from .models import Category, Event, EventGroup


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['user', ]


class EventGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = EventGroup
        fields = '__all__'
        read_only_fields = ['user', ]

