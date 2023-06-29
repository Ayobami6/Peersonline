from django import forms


class AskGPTForm(forms.Form):
    """ This class is used to create the ask gpt form
    """
    ask_gpt = forms.CharField(label='Ask GPT', max_length=1000)

    class Meta:
        fields = ('ask_gpt')
        widgets = {
            'ask_gpt': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ask Me Anything SE Related'}),
        }
