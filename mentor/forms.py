from django import forms
from .models import MentorSession
from .widgets import DateTimeSelectWidget


class MentorForm(forms.ModelForm):
    """ This class is used to create a mentor session form
    """
    time = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={'class': 'form-control', 'placeholder': '2023-01-01 00:00:00'},
    ),
        input_formats=['%Y-%m-%d %H:%M:%S']
    )

    class Meta:
        model = MentorSession
        fields = ['mentor_full_name', 'topic_title', 'description',
                  'venue', 'venue_link', 'time', 'duration', 'mentor']
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
            'duration':
                forms.NumberInput(
                    attrs={'class': 'form-control',
                           'placeholder': 'Duration'}),
            'mentor':
                forms.Select(attrs={'class': 'form-control'}),
        }
