from django import forms
from .models import Choice

class ChoiceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)
        for i, c in enumerate(Choice.objects.all()):
            self.fields['choice-' + str(i)] = forms.CharField(max_length=100, label=c.choice_text)
