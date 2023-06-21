from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from posts.models import Posts
from .forms import ProfileEditForm
from django.urls import reverse_lazy

# Create your views here.


@method_decorator(login_required(login_url='home/login'), name="get")
class HomeView(ListView):
    """ This class is used to view the home page
    """
    model = Posts
    context_object_name = 'posts'
    template_name = 'users/home.html'
    # oreder the posts by the most recent
    # ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        """ This method is used to get the context data """
        context = super().get_context_data(**kwargs)
        user_profile = self.request.user.profile
        context['user_profile'] = user_profile
        return context


class LoginAndSignUpView(LoginView):
    """ This class is used to view the login page """
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    """ This class is used to logout the user """
    success_url = 'home/login'
    redirect_url = "home/login"


class ProfileView(DetailView):
    """ This class is used to view the profile page """
    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        """ This method is used to get the context data """
        context = super().get_context_data(**kwargs)
        user_profile = self.request.user.profile
        context['user_profile'] = user_profile
        return context


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'users/profile_edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('home')
