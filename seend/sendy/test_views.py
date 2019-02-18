from django.shortcuts import reverse
from rest_framework.test import APITestCase
from sendy.models import RiderProfile

class TestRiderViews(APITestCase):
	def setUp(self):
		self.rider = RiderProfile(username="Keith Mandela", email="keith@olympians.com", contact_phone="09878", operation_area="Eastern Bypass")
		self.rider.save()

	def test_new_rider(self):
		response = se;f.client.post(reverse('parcels'), {
			"username": "Kelvin Kibet",
			"email": "kib@olympians.com",
			"contact_phone": "17655",
			"operation_area": "Survey",
			})
		self.assertEqual(RiderProfile.objects.count(), 2)
		self.assertEqual(201, response.status_code)

	def test_all_riders(self):
		response = self.client.get(reverse('riders', format="json"))
		self.assertEqual(len(response.data), 1)
		self.assertEqual(200, response.status_code)