from rest_framework import generics, permissions, response
from django.contrib.auth.models import User

from sendy.models import (
    EmployeeProfile, Parcel, RiderProfile, CustomerProfile)
from sendy.serializers import (
    EmployeeSerializer, ParcelSerializer, RiderSerializer, CustomerSerializer, UserSerializer)
from sendy.permissions import IsOwnerOrReadOnly, ReadOnly


class ParcelList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated|ReadOnly,)
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, format=None):
        content = {
            "status": "You do not have permission to view this resource"
        }
        return response.Response(content)

class OneParcel(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AllRiders(generics.ListCreateAPIView):
	"""Class to create a new rider and view all riders. """
	queryset = RiderProfile.objects.all()
	serializer_class = RiderSerializer

class Employee(generics.ListCreateAPIView):
    """ This class creates an endpoint for getting all employees
    and creating an employee
    """
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeEdit(generics.RetrieveUpdateAPIView):
    """ This class creates an endpoint for getting all employees
    and creating an employee
    """
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeSerializer


class Customer(generics.ListCreateAPIView):
    """This is class that manages the customer data"""
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerSerializer
