from django.shortcuts import render
from .forms import MentorForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import MentorSession


# Create your views here.

class MentorFormView(FormView):
    form_class = MentorForm
    template_name = 'mentor/mentor.html'
    success_url = reverse_lazy('mentor')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class MentorListView(ListView):
    model = MentorSession
    context_object_name = 'sessions'
    template_name = 'mentor/sessions.html'
    ordering = ['-time']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:20]