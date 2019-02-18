from rest_framework import serializers
from sendy.models import RiderProfile

class RiderSerializer(serializers.ModelSerializer):
	class Meta:
		model = RiderProfile
		fields = ('created', 'username', 'email', 'contact_phone', 'operation_area')



