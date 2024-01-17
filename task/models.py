from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from employee.models import Employee
from main.models import Department

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Task Category'
        verbose_name_plural = 'Task Categories'
        ordering = ['created']

    type = models.CharField(max_length=25)
    description = models.CharField(max_length=200, null=True, blank=True)
    source = models.CharField(max_length=25)

    created_by = models.ForeignKey(User, related_name="created_categories", null=True, on_delete=models.SET_NULL, default=1)
    updated_by = models.ForeignKey(User, related_name="updated_categories", null=True, on_delete=models.SET_NULL, default=1)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.type) + ' - ' + str(self.source)


class Task(models.Model):
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['created']

    STATUS = ('in-progress', 'pending', 'completed')

    title = models.CharField(max_length=25)
    slug = models.SlugField(blank=True, unique=True, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE, related_name='department_tasks')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name='category_tasks')
    parent_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='sub_tasks')

    start_time = models.DateTimeField(help_text='task started at ...', null=True, blank=False)
    end_time = models.DateTimeField(help_text='task ended at ...', null=True, blank=True)
    target_time = models.DateTimeField(help_text='task should be ended at ...', null=True, blank=False)
    assigned_to = models.ManyToManyField(Employee, blank=True, related_name="assigned_tasks")
    assigned_by = models.ForeignKey(Employee, null=True, related_name="assigned_by_tasks", on_delete=models.SET_NULL)
    supervisor = models.ForeignKey(Employee, null=True, related_name="supervised_tasks", on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, default='pending', choices=list(zip(STATUS, STATUS)))

    created_by = models.ForeignKey(Employee, related_name="created_tasks", null=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(Employee, related_name="updated_tasks", null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
