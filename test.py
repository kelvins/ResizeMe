from django.test import Client
from django.urls import reverse
import unittest

client = Client()

class TestResizeURLs(unittest.TestCase):

	def test_index(self):
		response = client.get('/')
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()