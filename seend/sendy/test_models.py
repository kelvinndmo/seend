from django.test import TestCase

from sendy.models import RiderProfile

# Create your tests here.
class TestRiderProfileModel(TestCase):
	""" Class for testing the RiderProfile model. """

	def setUp(self):
		""" Method creates a dummy rider to be used in testing. """
		self.rider = RiderProfile(username="Keith Mandela", email="keith@olympians.com", contact_phone="09878", operation_area="Eastern Bypass")
		self.rider.save()

	def test_rider_creation(self):
		""" Method tests rider creation. """
		self.assertEqual(self.rider.email, "keith@olympians.com")

	def test_rider_list(self):
		""" Method tests getting all riders. ""
		self.assertEqual(RiderProfile.objects.count(), 1)


