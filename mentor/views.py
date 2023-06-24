from django.shortcuts import render
from .forms import MentorForm
from django.views.generic import CreateView


# Create your views here.

class MentorView(CreateView):
    form_class = MentorForm
    template_name = 'mentor/mentor.html'
    success_url = '/mentor/register_session'
