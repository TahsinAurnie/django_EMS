# Generated by Django 4.2.6 on 2024-01-15 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_department_shifts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='office',
        ),
        migrations.DeleteModel(
            name='Office',
        ),
    ]