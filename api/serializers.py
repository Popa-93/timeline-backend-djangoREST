from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from .models import Activity, Record, Timeline


class ActivitySerializer(serializers.ModelSerializer):

    avatar = Base64ImageField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Activity
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Record
        fields = '__all__'


class TimelineSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Timeline
        fields = '__all__'
