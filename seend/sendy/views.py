from .serializers import ParcelSerializer
from .models import Parcel
from rest_framework import generics

class ParcelList(generics.ListCreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

class OneParcel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
