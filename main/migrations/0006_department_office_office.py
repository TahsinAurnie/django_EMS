# Generated by Django 4.2.6 on 2024-01-15 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_remove_contact_contact_number_contact_contact_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='office',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='office_departments', to='main.branch'),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkintime', models.TimeField(null=True, verbose_name='Check in time')),
                ('checkouttime', models.TimeField(null=True, verbose_name='Check out time')),
                ('tolerance', models.TimeField(null=True, verbose_name='tolerance time')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='branch_offices', to='main.branch')),
                ('created_by', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_offices', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_offices', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Office',
                'verbose_name_plural': 'Offices',
                'ordering': ['created_at'],
            },
        ),
    ]
