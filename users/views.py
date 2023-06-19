from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from posts.models import Posts

# Create your views here.


@method_decorator(login_required(login_url='home/login'), name="get")
class HomeView(ListView):
    model = Posts
    context_object_name = 'posts'
    template_name = 'users/home.html'

    def get_context_data(self, **kwargs):
        """ This method is used to get the context data """
        context = super().get_context_data(**kwargs)
        user_profile = self.request.user.profile
        context['user_profile'] = user_profile
        return context


class LoginAndSignUpView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    success_url = 'home/login'
    redirect_url = "home/login"
