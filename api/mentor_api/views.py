from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MentorSessionSerializer
from mentor.models import MentorSession

# Create your views here.


class MentorSessionViewSet(viewsets.ModelViewSet):
    serializer_class = MentorSessionSerializer
    queryset = MentorSession.objects.all().order_by('-created_at')
