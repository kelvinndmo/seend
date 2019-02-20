""" This module converts complex data to native Python data types """
from rest_framework import serializers

from .models import (
    RiderProfile, EmployeeProfile, Parcel, CustomerProfile)


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

class EmployeeSerializer(serializers.ModelSerializer):
    """This class is used to serialize Employee profile
    """
    class Meta:
        model = EmployeeProfile
        fields = ('created', 'username', 'email', 'contact_phone')


class CustomerSerializer(serializers.ModelSerializer):
    """""This class is used to serialize customer profile"""
    class Meta:
        model = CustomerProfile
        fields = ('created', 'username', 'email', 'contact_phone')
