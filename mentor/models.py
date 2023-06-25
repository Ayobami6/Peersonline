from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MentorSession(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    mentor_full_name = models.CharField(
        max_length=250,
        default=mentor)
    created_at = models.DateTimeField(auto_now_add=True)
    topic_title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    venue = models.CharField(max_length=250)
    venue_link = models.CharField(max_length=250)
    time = models.DateTimeField()
    duration = models.IntegerField(default=1)
