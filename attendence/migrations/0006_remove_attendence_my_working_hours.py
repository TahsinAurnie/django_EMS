# Generated by Django 4.2.6 on 2024-01-15 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0005_alter_attendence_my_working_hours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='my_working_hours',
        ),
    ]
