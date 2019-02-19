from rest_framework import generics

from sendy.models import (
    EmployeeProfile,Parcel, RiderProfile)
from sendy.serializers import (
    EmployeeSerializer, ParcelSerializer, RiderSerializer) 


class ParcelList(generics.ListCreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

class OneParcel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


class AllRiders(generics.ListCreateAPIView):
	"""Class to create a new rider and view all riders. """
	queryset = RiderProfile.objects.all()
	serializer_class = RiderSerializer

# Create your views here.
class Employee(generics.ListCreateAPIView):
    """ This class creates an endpoint for getting all employees
    and creating an employee
    """
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeSerializer
