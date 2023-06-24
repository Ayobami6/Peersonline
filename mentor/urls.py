from .views import MentorView
from django.urls import path

urlpatterns = [
    path('register_session', MentorView.as_view(), name='mentor'),
]
