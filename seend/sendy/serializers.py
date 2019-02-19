""" Converts Django data to JSON."""

from rest_framework import serializers
from sendy.models import RiderProfile


class RiderSerializer(serializers.ModelSerializer):
	"""Serializer class for the RiderProfile model. """
	class Meta:
		model = RiderProfile
		fields = ('created', 'username', 'email', 'contact_phone', 'operation_area')



