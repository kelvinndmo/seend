from rest_framework import generics, permissions, response
from django.contrib.auth.models import User

from sendy.models import (
    EmployeeProfile, Parcel, RiderProfile, CustomerProfile, AppUser, StaffUser)
from sendy.serializers import (
    EmployeeSerializer, ParcelSerializer, RiderSerializer, CustomerSerializer, AssignRiderSerializer, AppUserSerializer, StaffUserSerializer, ParcelStatusSerializer, ParcelDestinationSerializer)
from sendy.permissions import IsOwnerOrReadOnly, ReadOnly


class ParcelList(generics.ListCreateAPIView):
    permission_classes = (ReadOnly,)
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

class UserParcels(generics.ListAPIView):
    serializer_class = ParcelSerializer

    def get_queryset(self):
        user = self.request.user
        return Parcel.objects.filter(owner=user)

class UpdateParcelStatus(generics.RetrieveUpdateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelStatusSerializer

class UpdateParcelDestination(generics.RetrieveUpdateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelDestinationSerializer

class AssignRider(generics.RetrieveUpdateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = AssignRiderSerializer


class RegisterUser(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class RegisterStaff(generics.CreateAPIView):
    queryset = StaffUser.objects.all()
    serializer_class = StaffUserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AppUserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AppUserSerializer

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
