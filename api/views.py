from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator

from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import viewsets

from .models import Activity, Record
from .serializers import ActivitySerializer, RecordSerializer

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.views import LogoutView


# @method_decorator(csrf_exempt, name='dispatch')


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


# @method_decorator(csrf_protect, name='dispatch')
@permission_classes([IsAuthenticated])
class Logout(LogoutView):
    pass


# @csrf_protect
@permission_classes([IsAuthenticated])
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()  # TODO filter(user=) -> permissions
    serializer_class = ActivitySerializer
    # TODO Filter on user_id contained in the jwt token (in header)


@permission_classes([IsAuthenticated])
class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

# from rest_framework.views import APIView
# from rest_framework.response import Response

# class HelloView(APIView):
#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)
# + in Urls.py : path('hello/', views.HelloView.as_view(), name='hello'),
