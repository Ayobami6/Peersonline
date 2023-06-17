from django.urls import path
from .views import HomeView, LoginAndSignUpView, UserLogoutView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('home/login', LoginAndSignUpView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),

]
