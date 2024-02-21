from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class SignupTestCase(TestCase):
    def test_signup_success(self):
        url = reverse('signup')
        data = {
            'username': 'papi',
            'email': 'papi@test.com',
            'password': 'Nutr!P@pi2024'
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        user_exists = get_user_model().objects.filter(username=data['username']).exists()
        self.assertTrue(user_exists)

    def test_signup_failure(self):
        url = reverse('signup')
        data = {}  # Sending empty data
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
