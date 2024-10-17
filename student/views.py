from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import TaskExecuteForm

from accounts.models import Task, Course, Grade, Result


def view_grades(request):
    if request.user.is_authenticated and request.user.is_student:
        student = request.user.student
        grades = Grade.objects.filter(student=student)
        return render(request, 'grades.html', {'grades': grades})
    else:
        return render(request, 'error_page.html')

def task_list(request):
    if request.user.is_authenticated and request.user.is_student:
        student = request.user.student
        completed_tasks = Result.objects.filter(student=student).values_list('task_id', flat=True)
        context = {
            'completed_tasks': completed_tasks,
        }
        return render(request, 'list_task_for_student.html', context)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = context['object']
        student_has_result = Result.objects.filter(task=task, student=self.request.user.student).exists()
        context['student_has_result'] = student_has_result
        context['task_id'] = self.object.id
        return context

def task_execute(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskExecuteForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.task = task
            result.student = request.user.student  # Предполагается, что пользователь является студентом
            result.save()
            task.checked = False
            task.save()
            return redirect('task_detail', pk=task_id)
    else:
        form = TaskExecuteForm()
    return render(request, 'task_execute.html', {'task': task, 'form': form})
