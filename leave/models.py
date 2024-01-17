from django.db import models
from .managers import LeaveManager
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.


class Leave(models.Model):
    class Meta:
        verbose_name = _('Leave')
        verbose_name_plural = _('Leaves')
        ordering = ['-created']

    DAYS = 30
    LEAVE_TYPE = ('Sick Leave',
                  'Casual Leave',
                  'Emergency Leave',
                  'Study Leave',
                  'Maternity Leave',
                  'Compensatory Leave')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startdate = models.DateField(verbose_name=_('Start Date'), help_text='leave start date is on ..', null=True, blank=False)
    enddate = models.DateField(verbose_name=_('End Date'), help_text='coming back on ...', null=True, blank=False)
    leavetype = models.CharField(choices=list(zip(LEAVE_TYPE, LEAVE_TYPE)), max_length=25, default='Sick Leave', null=True, blank=False)
    reason = models.CharField(verbose_name=_('Reason for Leave'), max_length=255, help_text='add additional information for leave', null=True, blank=True)
    defaultdays = models.PositiveIntegerField(verbose_name=_('Leave days per year counter'), default=DAYS, null=True, blank=True)
    status = models.CharField(max_length=12, default='pending')
    is_approved = models.BooleanField(default=False)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = LeaveManager()

    def __str__(self):
        return str(self.leavetype) + ' - ' + str(self.user)

    @property
    def leave_days(self):
        startdate = self.startdate
        enddate = self.enddate
        if startdate > enddate:
            return 0
        dates = enddate - startdate
        return dates.days

    @property
    def leave_approved(self):
        return self.is_approved

    @property
    def approve_leave(self):
        if not self.is_approved:
            self.is_approved = True
            self.status = 'approved'
            self.save()

    @property
    def unapprove_leave(self):
        if self.is_approved:
            self.is_approved = False
            self.status = 'pending'
            self.save()

    @property
    def leaves_cancel(self):
        if self.is_approved or not self.is_approved:
            self.is_approved = False
            self.status = 'cancelled'
            self.save()

    @property
    def reject_leave(self):
        if self.is_approved or not self.is_approved:
            self.is_approved = False
            self.status = 'rejected'
            self.save()

    @property
    def is_rejected(self):
        return self.status == 'rejected'
