from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse

class MyViewTests(TestCase):
    def setUp(self):
        # Setup any data needed for your tests
        pass

    def test_my_view(self):
        # Create a test client
        client = Client()

        # Make a GET request to your view
        response = client.get(reverse('doctorlogin'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Optionally, you can check other things such as response content
        # For example, if your view returns some specific content
        self.assertContains(response, 'Expected content')

        # You can also check if certain template is being used
        self.assertTemplateUsed(response, 'doctor_login.html')


