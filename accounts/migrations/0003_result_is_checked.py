# Generated by Django 5.0.6 on 2024-06-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_course_students_enrollment_course_enrollments'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
    ]
