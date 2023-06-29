from django import forms
from .models import Profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name',
                  'bio', 'profile_pic', 'openai_key']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Last Name'}),
            'bio': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Write a short bio about yourself'}),
            'openai_key':
                forms.TextInput(attrs={'class': 'form-control',
                                       'placeholder': 'OpenAI API Key'}),
        }
