
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.views import LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Activity, Record, Timeline
from .serializers import (ActivitySerializer, RecordSerializer,
                          TimelineSerializer)


# @method_decorator(csrf_exempt, name='dispatch') TODO

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


# @method_decorator(csrf_protect, name='dispatch')
@permission_classes([IsAuthenticated])
class Logout(LogoutView):
    pass


# @csrf_protect
@ permission_classes([IsAuthenticated])
class TimelineViewSet(viewsets.ModelViewSet):
    serializer_class = TimelineSerializer

    def get_queryset(self):
        return Timeline.objects.filter(user=self.request.user.id)


@ permission_classes([IsAuthenticated])
class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = ActivitySerializer(
    #         data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)

    #     print("Validated =", serializer.validated_data)
    #     return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user.id)


@ permission_classes([IsAuthenticated])
class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer

    def create(self, request, *args, **kwargs):
        print("RecordViewSet.create")
        serializer = RecordSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        print("Validated =", serializer.validated_data)
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return Record.objects.filter(user=self.request.user.id)
