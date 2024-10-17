# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_teacher', 'is_student', 'is_admin', 'is_staff')
    list_filter = ('is_teacher', 'is_student', 'is_admin', 'is_staff')  # Исправьте здесь
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_teacher', 'is_student', 'is_admin', 'is_staff')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Task)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(LearningMaterial)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Result)
admin.site.register(Enrollment)
