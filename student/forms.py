from django import forms
from accounts.models import Result


class TaskExecuteForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['result']
