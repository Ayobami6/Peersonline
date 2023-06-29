from rest_framework import serializers
from mentor.models import MentorSession


class MentorSessionSerializer(serializers.ModelSerializer):
    """ This class is used to serialize the mentor session model
    """
    class Meta:
        model = MentorSession
        fields = '__all__'
