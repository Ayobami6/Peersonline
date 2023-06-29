from .views import MentorFormView, MentorListView
from django.urls import path

urlpatterns = [
    path('register_session', MentorFormView.as_view(), name='mentor'),
    path('sessions', MentorListView.as_view(), name='sessions'),
]
