# Generated by Django 5.0.6 on 2024-06-09 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_result_is_checked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, default='Название_Книги')),
                ('author', models.TextField(blank=True, default='Автор_Книги')),
                ('pages', models.IntegerField(blank=True, default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.course')),
            ],
        ),
    ]
