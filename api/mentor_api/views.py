from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import MentorSessionSerializer
from mentor.models import MentorSession
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.


class MentorSessionViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows mentor sessions to be retrieved or edited.
    """
    serializer_class = MentorSessionSerializer
    queryset = MentorSession.objects.all().order_by('-created_at')

    def list(self, request):
        """ List all mentor sessions
        """
        queryset = MentorSession.objects.all().order_by('-created_at')
        serializer = MentorSessionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ Create a new mentor session
        """
        serializer = MentorSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Retrieve a mentor session
        """
        queryset = MentorSession.objects.all()
        mentor_session = get_object_or_404(queryset, pk=pk)
        serializer = MentorSessionSerializer(mentor_session)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """ Update a mentor session
        """
        mentor_session = MentorSession.objects.get(pk=pk)
        serializer = MentorSessionSerializer(mentor_session, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """ Delete a mentor session
        """
        mentor_session = MentorSession.objects.get(pk=pk)
        mentor_session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
