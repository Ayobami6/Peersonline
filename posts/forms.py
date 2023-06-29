from .models import Posts
from django import forms


class PostsForms(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Title'}),
            'content': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Write your post here'}),
        }
