import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from mentor.models import MentorSession
from mentor.forms import MentorForm


@pytest.fixture
def create_mentor_session_data():
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
def test_create_mentor_session_view(client, create_mentor_session_data):
    user, session_data = create_mentor_session_data
    client.login(username='testuser', password='password')
    url = reverse('mentor')
    response = client.post(url, data=session_data)
    assert response.status_code == 302
    assert response.url == reverse('mentor')
    # check if the mentor session was created
    assert MentorSession.objects.filter(mentor=user.id,
                                        topic_title='test topic',
                                        description='test description',
                                        venue='test venue',).exists()
    sessions = MentorSession.objects.all()
    assert sessions.count() == 1


@pytest.mark.django_db
def test_register_session_url(client, create_mentor_session_data):
    user, session_data = create_mentor_session_data
    client.login(username='testuser', password='password')
    response = client.get(path='/register_session')
    assert response.status_code == 200
    assert 'mentor/mentor.html' in response.template_name
    assert isinstance(response.context['form'], MentorForm)
    assert 'Register' in str(response.content)


@pytest.mark.django_db
def test_sessions_list_url(client, create_mentor_session_data):
    user, session_data = create_mentor_session_data
    client.login(username='testuser', password='password')
    response = client.get(path='/sessions')
    assert response.status_code == 200
    assert 'mentor/sessions.html' in response.template_name
    assert 'sessions' in response.context
