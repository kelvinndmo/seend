""" These are ther models for SendIt APP"""

from django.db import models


# Create your models here.
class Parcel(models.Model):
    destination = models.CharField(max_length=60)
    origin = models.CharField(max_length=100)
    sender = models.CharField(max_length=120)
    recipient = models.CharField(max_length=100)
    recipient_phone = models.IntegerField()
    sender_phone = models.IntegerField()

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
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    contact_phone = models.IntegerField()
    operation_area = models.CharField(max_length=25)

    class Meta:
        ordering = ['created']

