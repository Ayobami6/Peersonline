import pytest
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from users.models import Profile


def test_home_login_redirect(client):
    """ Test that the home page redirects to login if not logged in """
    # Send a GET request to the home page
    response = client.get('/home')
    # confirm that the user is redirected to the login page if not logged in
    assert response.status_code == 302
    assert response.url == 'home/login?next=/home'


@pytest.mark.django_db
def test_login_view(client):
    """ Test that the login page loads correctly """
    # Send a GET request to the login page
    response = client.get(path='/home/login')
    # confirm the ok status
    assert response.status_code == 200
    # confirm that the login page is rendered
    assert 'Github' in str(response.content)
    assert 'Google' in str(response.content)
    assert 'users/login.html' in response.template_name


@pytest.mark.django_db
def test_user_logout_view_authenticated(client):
    """ Test that the user can log out """
    # Create a user for testing
    username = 'testuser'
    password = 'testpassword'
    User.objects.create_user(username=username, password=password)

    # Log in the user
    client.login(username=username, password=password)

    # Get the logout URL
    logout_url = reverse('logout')

    # Send a GET request to the logout URL
    response = client.post(logout_url)

    # Assert that the user is logged out
    assert response.status_code == 302  # Redirect status code
    assert response.url == '/home/login'  # Verify the redirect URL


@pytest.mark.django_db
def test_user_logout_view_unauthenticated(client):
    """ Test the logout view when the user is not logged in """
    # Get the logout URL
    logout_url = reverse('logout')

    # Send a GET request to the logout URL
    response = client.post(logout_url)

    # Assert that the user is redirected to the login page
    assert response.status_code == 302  # Redirect status code
    assert response.url == '/home/login'  # Verify the redirect URL


@pytest.mark.django_db
def test_profile_creation():
    """ Test that a profile is created automatically when a user is created """
    # Create a user
    user = User.objects.create(username='testuser')

    # Verify that a profile is created automatically
    assert Profile.objects.first().user == user
    assert Profile.objects.first().bio == ''
    assert Profile.objects.first().profile_pic == 'profile_pics/default.png'
    assert Profile.objects.first().openai_key == ''
    assert Profile.objects.first().first_name == ''
    assert Profile.objects.first().last_name == ''
    assert Profile.objects.count() == 1


@pytest.mark.django_db
def test_profile_str_representation():
    """ Test the __str__() method of the Profile model """
    # Create a user
    user = User.objects.create(username='testuser')

    # filter the profile of the user since the profie is automatically created
    # when a user is created with the post_save signal
    profile = Profile.objects.filter(user=user).first()

    # Verify the __str__() method returns the expected string representation
    expected_str = f'{user.username} Profile'
    assert str(profile) == expected_str


@pytest.mark.django_db
def test_profile_save_encryption():
    """ Test that the openai_key is encrypted when saving the profile """
    # Create a user
    user = User.objects.create(username='testuser')

    # a dummy openai_key
    openai_key = 'supersecretkey'
    # get the profile of the user
    profile = Profile.objects.filter(user=user).first()
    # set the openai_key
    profile.openai_key = openai_key
    # save the profile
    profile.save()
    # refresh the profile from the database
    profile.refresh_from_db()
    # Verify that the openai_key is encrypted when saving the profile
    assert profile.openai_key != openai_key
    assert profile.openai_key != ''
    assert profile.openai_key is not None
