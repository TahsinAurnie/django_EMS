from django.utils import timezone


def get_default_date():
    return timezone.now().date()
