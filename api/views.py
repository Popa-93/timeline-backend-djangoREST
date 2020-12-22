from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator

from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Activity, Record, Timeline
from .serializers import ActivitySerializer, RecordSerializer, TimelineSerializer

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.views import LogoutView


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
    def get_queryset(self):
        return Timeline.objects.filter(user=self.request.user.id)
    serializer_class = TimelineSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data | {"user": request.user.id})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print("serializer.data =", serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@ permission_classes([IsAuthenticated])
class ActivityViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user.id)

    serializer_class = ActivitySerializer


@ permission_classes([IsAuthenticated])
class RecordViewSet(viewsets.ModelViewSet):
    # TODO Add filter according to Timeline
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
