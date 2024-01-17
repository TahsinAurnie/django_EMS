# Generated by Django 4.2.6 on 2024-01-15 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_department_office_delete_office'),
        ('employee', '0006_alter_designation_options_alter_role_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designation',
            name='department',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_designations', to='main.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_employees', to='main.department'),
        ),
    ]
