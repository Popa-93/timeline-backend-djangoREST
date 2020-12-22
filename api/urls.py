from django.urls import path, re_path, include
from rest_framework import permissions, routers
from api.views import GoogleLogin, Logout, ActivityViewSet, RecordViewSet, TimelineViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from dj_rest_auth.urls import urlpatterns as dj_urlpatterns

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='Activity')
router.register(r'records', RecordViewSet, basename='Record')

timeline_list = TimelineViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
timeline_detail = TimelineViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = dj_urlpatterns + [
    # Google authentification
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('logout/', Logout.as_view(), name='rest_logout'),

    path('timelines/', timeline_list, name='timeline-list'),
    path('timelines/<int:pk>/', timeline_detail, name='timeline-detail'),

    #   re_path(r'^accounts/', include('allauth.urls'), name='socialaccount_signup'),
    # API Ressources URLs
    path('', include(router.urls)),
    # API swagger/redoc access
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
                                             cache_timeout=0), name='schema-redoc'),
]
