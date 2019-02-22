""" This module converts complex data to native Python data types """
from rest_framework import serializers
from django.contrib.auth.models import User

from sendy.models import (
    RiderProfile, EmployeeProfile, Parcel, CustomerProfile, AppUser, StaffUser)


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ("email", "username", "contact_phone", "user_type", "password")


class StaffUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffUser
        fields = ("email", "username", "contact_phone", "user_type", "password", "operation_area")


class ParcelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Parcel
        fields = (
            'destination','origin','sender_phone','recipient_phone','sender','recipient', 'owner', 'parcel_status', 'assigned_rider'
        )


class ParcelStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = (
            'parcel_status',
        )


class ParcelDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = (
            'destination',
        )


class AssignRiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = (
            'assigned_rider',
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
