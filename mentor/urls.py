from .views import MentorFormView
from django.urls import path

urlpatterns = [
    path('register_session', MentorFormView.as_view(), name='mentor'),
]
