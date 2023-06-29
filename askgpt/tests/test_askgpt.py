import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from askgpt.views import askgpt_view
from askgpt.forms import AskGPTForm

# test askgpt endpoint is user not logged in


@pytest.mark.django_db
def test_askgpt_url_unauthenticated(client):
    """ This function is used to test the askgpt url if not logged in
    """
    response = client.get(path='/askgpt/home/askgpt')
    assert response.status_code == 302
    assert response.url == '/home/login?next=/askgpt/home/askgpt'


@pytest.mark.django_db
def test_askgpt_url_authenticated(client):
    """ This function is used to test the askgpt url if logged in
    """
    user = User.objects.create_user(username='testuser', password='password')
    # login the user
    client.login(username='testuser', password='password')
    response = client.get(path='/askgpt/home/askgpt')
    assert response.status_code == 200
    assert 'Ask' in str(response.content)
