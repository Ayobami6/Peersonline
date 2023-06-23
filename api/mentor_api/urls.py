from django.urls import path, include
from rest_framework import routers
from api.mentor_api import views

router = routers.DefaultRouter()
router.register(r'mentor_sessions', views.MentorSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
