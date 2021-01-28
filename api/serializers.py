from rest_framework import serializers
from .models import Activity, Record, Timeline


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = '__all__'
        # extra_kwargs = {'user': {'required': False}}
        # unknown from front (kept in JWT cookie)
        #    -> get it from session once API call is authentified by JWT Cookie
