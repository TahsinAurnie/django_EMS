# Generated by Django 4.2.6 on 2024-01-16 12:25

import attendence.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0009_alter_attendence_checkintime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='date',
            field=models.DateField(default=attendence.utils.get_default_date),
        ),
    ]
