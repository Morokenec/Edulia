from django import forms
from accounts.models import Task, Course, Grade

class TaskForm(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label="Выберите курсс")

    class Meta:
        model = Task
        fields = ['title', 'description', 'checked', 'course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Название'
        self.fields['description'].label = 'Описание'
        self.fields['checked'].label = 'Отмечено'
        self.fields['course'].label = 'Курс'

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['grade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grade'].label = 'Оценка'