from django import forms
from .models import TestInfo


class TestForm(forms.ModelForm):
    class Meta:
        model = TestInfo
        fields = ['TestName', 'MaxMarks', 'TimeDuration', 'PosMarks', 'NegMarks', 'InputTextFile']
