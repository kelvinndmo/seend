from sendy.models import RiderProfile
from sendy.serializers import RiderSerializer
from rest_framework import generics

# Create your views here.
class AllRiders(generics.ListCreateAPIView):
	"""Class to create a new rider and view all riders. """
	queryset = RiderProfile.objects.all()
	serializer_class = RiderSerializer

