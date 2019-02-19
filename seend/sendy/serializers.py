from sendy.models import RiderProfile
from .models import Parcel
from rest_framework import serializers


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = (
            'destination','origin','sender_phone','recipient_phone','sender','recipient'
        )

class RiderSerializer(serializers.ModelSerializer):
	"""Serializer class for the RiderProfile model. """
	class Meta:
		model = RiderProfile
		fields = ('created', 'username', 'email', 'contact_phone', 'operation_area')

