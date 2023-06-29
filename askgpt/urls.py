from django.urls import path
from .views import askgpt_view as AskGPTView

urlpatterns = [
    path('home/askgpt', AskGPTView, name='ask'),
]
