from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User

from meeting.models import Conference


class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ('title', 'description', 'secret', 'beginDate', 'endDate')
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 5}),
        }
