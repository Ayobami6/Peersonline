from django.urls import path
from .views import HomeView, LoginAndSignUpView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginAndSignUpView.as_view(), name='login'),
]
