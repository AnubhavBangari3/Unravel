from django.test import TestCase
from django.conf import settings
from django.urls import reverse

# Create your tests here.

class ProfileTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # This method is run only once, before any other test.
        # It's purpose is to set data needed on a class-level.
        print('setUpTestData')
    def test_profile_url_exists(self):
        response = self.client.get("")
        
        self.assertEqual(response.status_code, 200)
        
   
        