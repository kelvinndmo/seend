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
        self.sender or self.destination
        
