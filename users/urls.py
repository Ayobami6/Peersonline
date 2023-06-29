from django.urls import path
from .views import (HomeView, LoginAndSignUpView,
                    UserLogoutView, ProfileView, ProfileEditView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home/login', LoginAndSignUpView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(),
         name='profile_edit'),
]
