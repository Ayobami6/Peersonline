from django.shortcuts import render
from .forms import MentorForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


# Create your views here.

class MentorFormView(FormView):
    form_class = MentorForm
    template_name = 'mentor/mentor.html'
    success_url = reverse_lazy('mentor')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
