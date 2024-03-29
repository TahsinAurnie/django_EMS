# Generated by Django 4.2.6 on 2024-01-14 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0004_alter_employee_contact_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='designation',
            name='level',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_employees', to=settings.AUTH_USER_MODEL),
        ),
    ]
