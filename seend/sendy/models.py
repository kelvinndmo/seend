from django.db import models

# Create your models here.

class RiderProfile(models.Model):
	"""Model for registering a rider. """"
	created = models.DateTimeField(auto_now_add=True)
	username = models.CharField(max_length=50)
	email = models.EmailField()
	contact_phone = models.IntegerField()
	operation_area = models.CharField(max_length=25)

	class Meta:
		ordering = ['created']