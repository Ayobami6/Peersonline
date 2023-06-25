from rest_framework import serializers
from mentor.models import MentorSession


class MentorSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorSession
        fields = '__all__'
