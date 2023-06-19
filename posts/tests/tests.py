import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from posts.models import Posts
from posts.forms import PostsForms
from posts.views import CreatePostView


@pytest.fixture
def create_post_data():
    """ This function is used to create a user and post form data """
    # create a user
    user = User.objects.create_user(
        username='testuser', email='test@gmail.com', password='password')
    # create a post form data
    form_data = {'title': 'test post', 'content': 'test content'}
    return user, form_data


@pytest.mark.django_db
def test_create_post_view(client, create_post_data):
    """ This function is used to test the create post view """
    # get the user and form data
    user, form_data = create_post_data
    # login the user
    client.login(username='testuser', password='password')
    # get the url for creating a post
    url = reverse('create_post')
    # post the form data
    response = client.post(url, data=form_data)
    # check the status code and redirect url
    assert response.status_code == 302
    assert response.url == reverse('home')
    # check if the post was created
    assert Posts.objects.filter(author=user, title='test post',
                                content='test content').exists()


@pytest.mark.django_db
def test_create_post_url_unauthenicated(client):
    """ This function is used to test the create post url if not logged in """
    # send a get request to the create post url
    response = client.get(path='/posts/home/create_post')
    assert response.status_code == 302
    assert response.url == '/accounts/login/?next=/posts/home/create_post'


@pytest.mark.django_db
def test_create_post_url_isauthenticated(client):
    """ This function is used to test the create post url if logged in """
    # create a user
    user = User.objects.create_user(
        username='testuser', password='password')
    # login the user
    client.login(username='testuser', password='password')
    response = client.get(path='/posts/home/create_post')
    assert response.status_code == 200
    assert 'posts/create_post.html' in response.template_name
    assert isinstance(response.context['form'], PostsForms)
    assert 'content' in str(response.content)


@pytest.mark.django_db
def test_post_detail_view(client, create_post_data):
    """ Test that the post detail page loads correctly """
    # get the user and form data
    user, form_data = create_post_data
    # login the user
    client.login(username='testuser', password='password')
    post = Posts.objects.create(
        author=user, title='test post', content='test content')
    response = client.get(path=f'/posts/home/post/{post.id}')
    # confirm the ok status
    assert response.status_code == 200
    # confirm that the post detail page is rendered
    assert 'posts/post_detail.html' in response.template_name
    assert 'content' in str(response.content)
    assert 'title' in str(response.content)


@pytest.mark.django_db
def test_post_update_view(client, create_post_data):
    user, form_data = create_post_data
    # login the user
    client.login(username='testuser', password='password')
    post = Posts.objects.create(
        author=user, title='test update this',
        content='test this should be updated')
    url = reverse('post_update', kwargs={'pk': post.id})
    response = client.post(url, data=form_data)
    assert response.status_code == 302
    assert response.url == reverse('home')
    post.refresh_from_db()
    assert post.title != 'test update this'
    assert post.title == 'test post'
    assert post.content != 'test this should be updated'
    assert post.content == 'test content'
