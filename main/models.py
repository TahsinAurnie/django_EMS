from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.validators import RegexValidator

# Create your models here.


class Address(models.Model):
    class Meta:
        verbose_name_plural = 'Addresses'
        verbose_name = 'Address'
        ordering = ['city', '-created_at']

    ADDRESS_TYPES = ('Permanent', 'Present')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    street_address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)
    long = models.CharField(max_length=100, blank=True, null=True)
    address_types = models.CharField(max_length=20, choices=list(zip(ADDRESS_TYPES, ADDRESS_TYPES)))
    is_primary = models.BooleanField(default=True)

    created_by = models.ForeignKey(User, related_name="created_addresses", null=True, on_delete=models.SET_NULL, default=1)
    updated_by = models.ForeignKey(User, related_name="updated_addresses", null=True, on_delete=models.SET_NULL, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_full_address

    @property
    def get_full_address(self):
        street_address = self.street_address
        city = self.city

        if street_address and city:
            fulladdress = str(street_address) + ',' + str(city)
            return fulladdress
        return


class Contact(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-created_at']

    CONTACT_TYPES = ('Mobile', 'Phone', 'email')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # contact_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Contact number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # contact_number = models.CharField(validators=[contact_regex], max_length=17, blank=True)
    contact_info = models.CharField(max_length=17, blank=True)
    contact_types = models.CharField(max_length=20, choices=list(zip(CONTACT_TYPES, CONTACT_TYPES)))
    is_primary = models.BooleanField(default=True)

    created_by = models.ForeignKey(User, related_name="created_contacts", null=True, on_delete=models.SET_NULL, default=1)
    updated_by = models.ForeignKey(User, related_name="updated_contacts", null=True, on_delete=models.SET_NULL, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_info


class Branch(models.Model):
    class Meta:
        verbose_name_plural = 'Branches'
        verbose_name = 'Branch'
        ordering = ['name']

    name = models.CharField(max_length=100, unique=True, error_messages={'unique': "The branch name must be unique"})
    parent_branch = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='sub_branches')
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL, related_name='branch_addresses')
    contact_info = models.ForeignKey(Contact, null=True, on_delete=models.SET_NULL, related_name='branch_contacts')

    created_by = models.ForeignKey(User, related_name="created_branches", null=True, on_delete=models.SET_NULL, default=1)
    updated_by = models.ForeignKey(User, related_name="updated_branches", null=True, on_delete=models.SET_NULL, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# class Office(models.Model):
#     class Meta:
#         verbose_name = 'Office'
#         verbose_name_plural = 'Offices'
#         ordering = ['created_at']
#
#     branch = models.ForeignKey(Branch, null=True, on_delete=models.SET_NULL, related_name='branch_offices')
#     checkintime = models.TimeField(verbose_name=_('Check in time'), null=True, blank=False)
#     checkouttime = models.TimeField(verbose_name=_('Check out time'), null=True, blank=False)
#     tolerance = models.TimeField(verbose_name=_('tolerance time'), null=True, blank=False)
#     created_by = models.ForeignKey(User, related_name="created_offices", null=True, on_delete=models.SET_NULL, default=1)
#     updated_by = models.ForeignKey(User, related_name="updated_offices", null=True, on_delete=models.SET_NULL, default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.id


class Department(models.Model):
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ['name', 'created_at']

    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125, null=True, blank=True)
    branch = models.ForeignKey(Branch, null=True, on_delete=models.SET_NULL, related_name='branch_departments')
    # office = models.ForeignKey(Branch, null=True, on_delete=models.SET_NULL, related_name='office_departments')
    shift = models.CharField(max_length=20, null=True, blank=True)

    created_by = models.ForeignKey(User, related_name="created_departments", null=True, on_delete=models.SET_NULL, default=1)
    updated_by = models.ForeignKey(User, related_name="updated_departments", null=True, on_delete=models.SET_NULL, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + "-" + self.shift









