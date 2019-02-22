""" These are ther models for SendIt APP"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, contact_phone, user_type, password):
        if not email:
            raise ValueError('Email address required')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            contact_phone=contact_phone,
            user_type=user_type,
            password=password,
        )

        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, contact_phone, password):
        user = self.create_user(
            email,
            username=username,
            contact_phone=contact_phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class AppUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=50)
    contact_phone = models.IntegerField()
    user_type = models.CharField(max_length=15, default="customer")
    password = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'username', 'user_type', 'contact_phone']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True


class StaffUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=50)
    contact_phone = models.IntegerField()
    user_type = models.CharField(max_length=15, default="employee")
    password = models.CharField(max_length=25)
    operation_area = models.CharField(max_length=15, default="Westlands")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'username', 'user_type', 'contact_phone', 'operation_area']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

class Parcel(models.Model):
    status_dict = {
        "status_1": "Awaiting Rider Pickup",
        "status_2": "Rider Assigned. On Transit",
        "status_3": "Awaiting Pickup",
        "status_4": "Delivered",
        "status_5": "Cancelled"
        }
    destination = models.CharField(max_length=60)
    origin = models.CharField(max_length=100)
    sender = models.CharField(max_length=120)
    recipient = models.CharField(max_length=100)
    recipient_phone = models.IntegerField()
    sender_phone = models.IntegerField()
    parcel_status = models.CharField(max_length=30, default=status_dict["status_1"])
    assigned_rider = models.CharField(max_length=30, default="No Rider Assigned")
    # assigned_rider = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned_parcels', on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey('auth.User', related_name='parcels', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Parcel, self).save(*args, **kwargs)

    def __str__(self):
        return self.sender or self.destination
        

class RiderProfile(models.Model):
    """Model for registering a rider. """
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    contact_phone = models.IntegerField()
    operation_area = models.CharField(max_length=25)

    class Meta:
        ordering = ['created']


class EmployeeProfile(models.Model):
    """Model for employee"""
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    contact_phone = models.IntegerField()
    operation_area = models.CharField(max_length=25)

    class Meta:
        ordering = ['created']


class CustomerProfile(models.Model):
    """Model for customer"""
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    contact_phone = models.IntegerField()

    class Meta:
        ordering = ['created']
