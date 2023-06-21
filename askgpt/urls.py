from django.urls import path
from .views import AskGPTView

urlpatterns = [
    path('home/askgpt', AskGPTView, name='ask'),
]
