from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import DietaryRestriction


class SignupTestCase(TestCase):
    def test_signup_success(self):
        url = reverse('signup')
        data = {
            'username': 'papi',
            'email': 'papi@test.com',
            'password': 'Nutr!P@pi2024',
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        
        User = get_user_model()
        user = User.objects.get(username=data['username'])
        self.assertTrue(user)
        self.assertEqual(user.target_weight, 80.0)
        self.assertEqual(user.current_weight, 80.0)

class SigninViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        User.objects.create_user(username='testuser', email='test@example.com', password='testpassword123')

    def test_signin_success(self):
        url = reverse('signin')
        data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_signin_failure(self):
        url = reverse('signin')
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

class LoggedInViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword123')
        self.client.login(username='testuser', password='testpassword123')

    def test_action_requires_login(self):
        self.client.logout() 
        url = reverse('loggedin')
        response = self.client.post(url, {}, content_type='application/json')
        self.assertEqual(response.status_code, 302)

    def test_logged_in_action(self):
        url = reverse('loggedin')
        data = {'caloriesConsumed': 500}
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('caloriesConsumed'), 500)

class UserInfoViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword123', email='test@example.com')
        self.client.login(username='testuser', password='testpassword123')

    def test_update_user_info(self):
        url = reverse('user_info')
        data = {'target_weight': 70}
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.target_weight, 70)

    def test_get_user_info(self):
        url = reverse('user_info')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)