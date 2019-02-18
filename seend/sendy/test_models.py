from django.test import TestCase
from sendy.models import RiderProfile

# Create your tests here.
class TestRiderProfileModel(TestCase):
	def setUp(self):
		self.rider = RiderProfile(username="Keith Mandela", email="keith@olympians.com", contact_phone="09878", operation_area="Eastern Bypass")
		self.rider.save()

	def test_rider_creation(self):
		self.assertEqual(self.rider.email, "keith@olympians.com")

	def test_rider_list(self):
		self.assertEqual(RiderProfile.objects.count(), 1)


