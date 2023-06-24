from django import forms
from .models import MentorSession


class MentorForm(forms.ModelForm):
    class Meta:
        model = MentorSession
        fields = ['mentor_full_name', 'topic_title', 'description',
                  'venue', 'venue_link', 'time', 'duration']
        widgets = {
            'mentor_full_name':
                forms.TextInput(
                    attrs={'class': 'form-control',
                           'placeholder': 'Full Name'}),
            'topic_title':
                forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description':
                forms.Textarea(
                    attrs={'class': 'form-control', 'placeholder':
                           'Describe your session'}),
            'venue':
                forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Venue'}),
            'venue_link':
                forms.TextInput(
                    attrs={'class': 'form-control',
                           'placeholder': 'Venue Link'}),
            'time':
                forms.DateTimeInput(
                    attrs={'class': 'form-control', 'placeholder': 'Time'}),
            'duration':
                forms.NumberInput(
                    attrs={'class': 'form-control',
                           'placeholder': 'Duration'}),
        }
