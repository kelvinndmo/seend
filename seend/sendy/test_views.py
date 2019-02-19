from django.shortcuts import reverse
from rest_framework.test import APITestCase

from sendy.models import RiderProfile

def check_if_empty(post_dict):
	if post_dict["username"] == "":
		return 'username'
	elif post_dict["operation_area"] == "":
		print("happy")


class TestRiderViews(APITestCase):
	""" This class tests Rider views. """
	def setUp(self):
		""" A method that creates a dummy rider to be used while testing. """
		self.rider = RiderProfile(username="Keith Mandela", email="keith@olympians.com", contact_phone="09878", operation_area="Eastern Bypass")
		self.rider.save()

	def test_new_rider(self):
		""" A method that tests response when creating new rider. """
		response = self.client.post(reverse('riders'), {
			"username": "Kelvin Kibet",
			"email": "kib@olympians.com",
			"contact_phone": "17655",
			"operation_area": "Survey",
			})
		self.assertEqual(RiderProfile.objects.count(), 2)
		self.assertEqual(201, response.status_code)

	def test_wrong_email(self):
		""" A method that tests response when an invalid email is entered. """
		response = self.client.post(reverse('riders'), {
			"username": "Kelvin Kibet",
			"email": "kibolympians.com",
			"contact_phone": "17655",
			"operation_area": "Survey",
			})
		self.assertEqual(response.status_code, 400)
		self.assertEqual(str(response.data["email"]), "[ErrorDetail(string='Enter a valid email address.', code='invalid')]")

	def test_string_phone(self):
		""" A method that tests response when a string is entered as contact_phone. """
		response = self.client.post(reverse('riders'), {
			"username": "Kelvin Kibet",
			"email": "kibolympians.com",
			"contact_phone": "nnnnn",
			"operation_area": "Survey",
			})
		self.assertEqual(response.status_code, 400)
		self.assertEqual(str(response.data["contact_phone"]), "[ErrorDetail(string='A valid integer is required.', code='invalid')]")

	def test_missing_name(self):
		""" A method that tests response when no username is entered. """
		post_dict = {
			"username": "",
			"email": "kibolympians.com",
			"contact_phone": "1233556",
			"operation_area": "Mwiki",
			}
		response = self.client.post(reverse('riders'), post_dict)
		missing_item = check_if_empty(post_dict)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(str(response.data[missing_item]), "[ErrorDetail(string='This field may not be blank.', code='blank')]")

	def test_missing_operation_area(self):
		""" A method that tests response when no operation area is entered. """
		post_dict = {
			"username": "Kelvin Kibet",
			"email": "kibolympians.com",
			"contact_phone": "1233556",
			"operation_area": "",
			}
		response = self.client.post(reverse('riders'), post_dict)
		missing_item = check_if_empty(post_dict)
		self.assertEqual(response.status_code, 400)
		self.assertEqual(str(response.data[missing_item]), "[ErrorDetail(string='This field may not be blank.', code='blank')]")

	def test_all_riders(self):
		""" A method that tests response when getting all riders. """
		response = self.client.get(reverse('riders'), format="json")
		self.assertEqual(len(response.data), 1)
		self.assertEqual(200, response.status_code)

		