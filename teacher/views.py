from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.models import Task, Course, Result, Student
from .forms import TaskForm, GradeForm


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.checked = False
            task.save()
            return redirect('lms-home')  # Замените 'task_list' на имя вашего URL-шаблона для списка задач
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

class TeacherTaskResultsView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_teacher

    def get(self, request):
        courses = Course.objects.filter(teacher__user=request.user)
        tasks = Task.objects.filter(course__in=courses)
        results = Result.objects.filter(task__in=tasks)

        context = {
            'courses': courses,
            'tasks': tasks,
            'results': results,
        }

        return render(request, 'results_list.html', context)


def grade_task(request, task_id, student_id):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            task = get_object_or_404(Task, id=task_id)
            student = get_object_or_404(Student, id=student_id)
            grade = form.save(commit=False)
            grade.task = task
            grade.student = student
            grade.save()
            return redirect('teacher_task_results')  # Перенаправление на страницу результатов
    else:
        form = GradeForm()
    return render(request, 'results_list.html', {'form': form})