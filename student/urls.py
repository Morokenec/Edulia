from . import views
from django.urls import path

urlpatterns = [
    path('list_task/', views.task_list, name='task_list_student'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:task_id>/execute/', views.task_execute, name='task_execute'),
    path('grades/', views.view_grades, name='view_grades'),
]
