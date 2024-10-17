from django.urls import path
from .views import create_task, TeacherTaskResultsView, grade_task

urlpatterns = [
    path('create_task/', create_task, name='create_task'),
    path('task-results/', TeacherTaskResultsView.as_view(), name='teacher_task_results'),
    path('grade-task/<int:task_id>/<int:student_id>/', grade_task, name='grade_task'),
]
