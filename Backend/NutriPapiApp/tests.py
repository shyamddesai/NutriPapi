from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Fridge, Ingredient

class SignupTestCase(TestCase):
    def test_signup_success(self):
        url = reverse('signup')
        data = {
            'username': 'papi',
            'email': 'papi@test.com',
            'password': 'Nutr!P@pi2024',
        }
        response = self.client.post(url, data, content_type='application/json')
        # print("Response: ", response)
        self.assertEqual(response.status_code, 201)
        
        User = get_user_model()
        user = User.objects.get(username=data['username'])
        # print("User.username: ", user.username)
        # print("User.email: ", user.email)
        # print("User.password: ", user.password)
        self.assertEqual(user.username, data['username'])
        self.assertEqual(user.email, data['email'])
        self.assertTrue(user.check_password(data['password']))

class SignupFollowViewTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_post_signup_follow(self):
        self.client.force_login(self.user)
        url = reverse('signup_follow')

        post_data = {
            'somekey': 'somevalue'  # Your view doesn't seem to use the posted data
        }

        response = self.client.post(url, json.dumps(post_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.content)
        self.assertEqual(response_data['id'], self.user.id)
        self.assertEqual(response_data['username'], self.user.username)

    def test_post_signup_follow_no_post(self):
        response = self.client.get(reverse('signup_follow'))
        self.assertEqual(response.status_code, 405)
        response_data = json.loads(response.content)
        self.assertEqual(response_data['error'], 'Only POST requests are allowed')

# class SigninViewTests(TestCase):
#     def setUp(self):
#         User = get_user_model()
#         User.objects.create_user(username='testuser', email='test@example.com', password='testpassword123')

#     def test_signin_success(self):
#         url = reverse('signin')
#         data = {
#             'username': 'testuser',
#             'password': 'testpassword123'
#         }
#         response = self.client.post(url, data, content_type='application/json')
#         self.assertEqual(response.status_code, 200)

#     def test_signin_failure(self):
#         url = reverse('signin')
#         data = {
#             'username': 'testuser',
#             'password': 'wrongpassword'
#         }
#         response = self.client.post(url, data, content_type='application/json')
#         self.assertEqual(response.status_code, 400)

# class LoggedInViewTests(TestCase):
#     def setUp(self):
#         User = get_user_model()
#         self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword123')
#         self.client.login(username='testuser', password='testpassword123')

#     def test_action_requires_login(self):
#         self.client.logout() 
#         url = reverse('loggedin')
#         response = self.client.post(url, {}, content_type='application/json')
#         self.assertEqual(response.status_code, 302)

#     def test_logged_in_action(self):
#         url = reverse('loggedin')
#         data = {'caloriesConsumed': 500}
#         response = self.client.post(url, data, content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json().get('caloriesConsumed'), 500)

# class UserInfoViewTests(TestCase):
#     def setUp(self):
#         User = get_user_model()
#         self.user = User.objects.create_user(username='testuser', password='testpassword123', email='test@example.com')
#         self.client.login(username='testuser', password='testpassword123')

#     def test_update_user_info(self):
#         url = reverse('user_info')
#         data = {'target_weight': 70}
#         response = self.client.post(url, data, content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.user.refresh_from_db()
#         self.assertEqual(self.user.target_weight, 70)

#     def test_get_user_info(self):
#         url = reverse('user_info')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)

# class FridgeAddIngredientsTests(TestCase):
#     def setUp(self):
#         User = get_user_model()
#         self.user = User.objects.create_user(username='testuser', password='testpass')
#         self.fridge = Fridge.objects.create(user=self.user)
#         self.client.login(username='testuser', password='testpass')

#     def test_add_ingredient_to_fridge(self):
#         url = reverse('add_ingredients_to_fridge')
#         data = {'name': 'Tomato', 'quantity': 3}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, 201)
#         self.assertTrue(Ingredient.objects.filter(name='Tomato').exists())

#     def test_add_ingredient_to_nonexistent_fridge(self):
#         url = reverse('add_ingredients_to_fridge')
#         data = {'name': 'Tomato', 'quantity': 3}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, 404)