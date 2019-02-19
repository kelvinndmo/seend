from .models import Parcel
from rest_framework import serializers


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = (
            'destination','origin','sender_phone','recipient_phone','sender','recipient'
        )