import datetime
from django.db import models
from django.contrib.auth.models import User
from main.models import Department, Address, Contact
from .managers import EmployeeManager

# Create your models here.


class Role(models.Model):
    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
        ordering = ['created_at']

    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125, null=True, blank=True)

    created_by = models.ForeignKey(User, related_name="created_roles", null=True, on_delete=models.SET_NULL, default=1)
    updated_by = models.ForeignKey(User, related_name="updated_roles", null=True, on_delete=models.SET_NULL, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Designation(models.Model):
    class Meta:
        verbose_name = 'Designation'
        verbose_name_plural = 'Designations'
        ordering = ['created_at']

    level = models.CharField(max_length=20)
    title = models.CharField(max_length=125)
    description = models.CharField(max_length=125, null=True, blank=True)
    department = models.ForeignKey(Department, related_name="department_designations", on_delete=models.CASCADE, null=True, default=None)

    created_by = models.ForeignKey(User, related_name="created_designations", null=True, on_delete=models.SET_NULL, default=1)
    updated_by = models.ForeignKey(User, related_name="updated_designations", null=True, on_delete=models.SET_NULL, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_full_designation

    @property
    def get_full_designation(self):
        level = self.level
        title = self.title

        if level and title:
            full = str(level) + ' ' + str(title)
            return full
        else:
            return title


class Employee(models.Model):
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['-created']

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    NOT_KNOWN = 'Not Known'

    GENDER = ('Male', 'Female', 'Other', 'Not Known')

    EMPLOYEETYPE = ('Full-Time', 'Part-Time', 'Contract', 'Intern')

    # PERSONAL DATA
    user = models.OneToOneField(User, related_name="user_employee", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="profile_images", default='default.png', help_text='upload image size less than 2.0MB')  # work on path username-date/image
    firstname = models.CharField(max_length=125, null=False, blank=False)
    lastname = models.CharField(max_length=125, null=False, blank=False)
    othername = models.CharField(max_length=125, null=True, blank=True)
    birthday = models.DateField(blank=False, null=False)
    gender = models.CharField(max_length=15, choices=list(zip(GENDER, GENDER)), blank=False, null=True)

    department = models.ForeignKey(Department, related_name='department_employees', on_delete=models.SET_NULL, null=True, default=None)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, default=None)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, default=None)
    supervisor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='supervisor_employees')
    personal_address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.SET_NULL, related_name='employee_addresses')
    contact_info = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.SET_NULL, related_name='employee_contacts')

    startdate = models.DateField(help_text='date of employement', blank=True, null=True)
    employeetype = models.CharField(max_length=15, default='Full-Time', choices=list(zip(EMPLOYEETYPE, EMPLOYEETYPE)), blank=False, null=True)

    employeeid = models.CharField(max_length=10, null=True, blank=True)
    dateissued = models.DateField(help_text='date staff id was issued', blank=False, null=True)

    is_blocked = models.BooleanField(help_text='button to toggle employee block and unblock', default=False)
    is_deleted = models.BooleanField(help_text='button to toggle employee deleted and undelete', default=False)

    created_by = models.ForeignKey(User, related_name="created_employees", null=True, on_delete=models.SET_NULL, default=1)
    updated_by = models.ForeignKey(User, related_name="updated_employees", null=True, on_delete=models.SET_NULL, default=1)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    # PLUG MANAGERS
    objects = EmployeeManager()

    def __str__(self):
        return self.get_full_name

    @property
    def get_full_name(self):
        firstname = self.firstname
        lastname = self.lastname
        othername = self.othername

        if (firstname and lastname) or othername is None:
            fullname = str(firstname) + ' ' + str(lastname)
            return fullname
        elif othername:
            fullname = str(firstname) + ' ' + str(lastname) + ' ' + str(othername)
            return fullname
        return

    @property
    def get_profile_picture(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

    @property
    def get_age(self):
        current_year = datetime.date.today().year
        dateofbirth_year = self.birthday.year
        if dateofbirth_year:
            return current_year - dateofbirth_year
        return
