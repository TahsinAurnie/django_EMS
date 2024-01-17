from django.db import models


class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def all_employees(self):
        return super().get_queryset()

    def all_blocked_employees(self):
        return super().get_queryset().filter(is_blocked=True)
