from django import forms


class DateTimeSelectWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            forms.Select(attrs={'class': 'datetime-select',
                         'style': 'width: 60px;'}),
            forms.Select(attrs={'class': 'datetime-select',
                         'style': 'width: 60px;'}),
            forms.Select(attrs={'class': 'datetime-select',
                         'style': 'width: 60px;'}),
            forms.Select(attrs={'class': 'datetime-select',
                         'style': 'width: 60px;'}),
            forms.Select(attrs={'class': 'datetime-select',
                         'style': 'width: 60px;'}),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.year, value.month,
                    value.day, value.hour, value.minute]
        return [None, None, None, None, None]

    def format_output(self, rendered_widgets):
        return '<div class="datetime-select-container">\
            {}</div>'.format(''.join(rendered_widgets))
