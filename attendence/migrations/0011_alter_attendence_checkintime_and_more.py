# Generated by Django 4.2.6 on 2024-01-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0010_alter_attendence_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='checkintime',
            field=models.TimeField(null=True, verbose_name='Check in time'),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='checkouttime',
            field=models.TimeField(null=True, verbose_name='Check out time'),
        ),
    ]