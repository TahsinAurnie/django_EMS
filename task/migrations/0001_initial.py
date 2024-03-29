# Generated by Django 4.2.6 on 2024-01-14 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0004_address_created_by_address_updated_by_and_more'),
        ('employee', '0006_alter_designation_options_alter_role_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=25)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('source', models.CharField(max_length=25)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_categories', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Task Category',
                'verbose_name_plural': 'Task Categories',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('start_time', models.DateTimeField(help_text='task started at ...', null=True)),
                ('end_time', models.DateTimeField(blank=True, help_text='task ended at ...', null=True)),
                ('target_time', models.DateTimeField(help_text='task should be ended at ...', null=True)),
                ('status', models.CharField(choices=[('In-progress', 'In-progress'), ('Pending', 'Pending'), ('Completed', 'Completed')], max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('assigned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_by_tasks', to='employee.employee')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tasks', to='employee.employee')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_tasks', to='task.category')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_tasks', to='employee.employee')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_tasks', to='main.department')),
                ('parent_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_tasks', to='task.task')),
                ('supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervised_tasks', to='employee.employee')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_tasks', to='employee.employee')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['created'],
            },
        ),
    ]
