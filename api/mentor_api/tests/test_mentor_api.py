import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from mentor.models import MentorSession
from mentor.forms import MentorForm


@pytest.fixture
def create_mentor_session_data():
    """ Pytest fixture for mentor session data, and user
    """
    user = User.objects.create_user(username='testuser', password='password')
    session_data = {'mentor': user.id,
                    'mentor_full_name': 'testuser',
                    'topic_title': 'test topic',
                    'description': 'test description',
                    'venue': 'test venue',
                    'venue_link': 'test venue link',
                    'time': '2020-05-05 12:00:00',
                    'duration': 1}
    return user, session_data


@pytest.mark.django_db
def test_api_endpoint_get(client):
    """ Test to check if the api endpoint is working
    """
    response = client.get(path='/api/mentor_sessions/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.django_db
def test_api_endpoint_post(client, create_mentor_session_data):
    """ Test to check if the api endpoint is working
    """
    user, session_data = create_mentor_session_data
    response = client.post(path='/api/mentor_sessions/', data=session_data)
    assert response.status_code == 201
    assert response.json()['mentor'] == user.id
    assert response.json()['mentor_full_name'] == 'testuser'
    assert response.json()['topic_title'] == 'test topic'
    assert response.json()['description'] == 'test description'
