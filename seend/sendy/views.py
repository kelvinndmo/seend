from rest_framework import generics

from .models import (
    EmployeeProfile, Parcel, RiderProfile, CustomerProfile)
from .serializers import (
    EmployeeSerializer, ParcelSerializer, RiderSerializer, CustomerSerializer)


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

# Create customer


class Customer(generics.ListCreateAPIView):
    """This is class that manages the customer data"""
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerSerializer
