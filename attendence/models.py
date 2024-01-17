from django.db import models
from datetime import datetime
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

from attendence.utils import get_default_date

# Create your models here.


class Attendence(models.Model):
    class Meta:
        verbose_name = _('Attendence')
        verbose_name_plural = _('Attendences')
        ordering = ['-created']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=get_default_date)
    shift = models.CharField(max_length=20, blank=True, null=True)
    checkintime = models.TimeField(verbose_name=_('Check in time'), null=True, blank=False)
    checkouttime = models.TimeField(verbose_name=_('Check out time'), null=True, blank=False)
    status = models.BooleanField(default=False)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    # objects = AttendanceManager()

    def __str__(self):
        return str(self.user) + ' - ' + str(self.total_working_hours)

    def calculate_working_hours(self):
        if self.checkintime and self.checkouttime:
            checkin_datetime = datetime.combine(self.date, self.checkintime)
            checkout_datetime = datetime.combine(self.date, self.checkouttime)

            # Calculate the time difference
            time_difference = checkout_datetime - checkin_datetime

            # Extract hours and minutes from the timedelta
            total_hours, remainder = divmod(time_difference.seconds, 3600)
            total_minutes = remainder // 60

            return total_hours, total_minutes
        else:
            return None

    @property
    def total_working_hours(self):
        working_hours = self.calculate_working_hours()
        if working_hours:
            return f'{working_hours[0]} hrs and {working_hours[1]} mins'
        else:
            return 0


