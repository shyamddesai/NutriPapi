from datetime import timedelta
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Ingredient, Fridge, Recipe, Schedule
from unittest.mock import patch
import pytz
import json

User = get_user_model()

class UserTests(TestCase):
    def setUp(self):
        """Create a user and log them in for testing."""
        self.base_url = reverse('signup')
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password123')
        self.client.login(username='testuser', password='password123')

    def test_signup_view(self):
        """Test the signup view for creating a new user."""
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpassword123'
        }
        response = self.client.post(self.base_url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_signup_follow(self):
        """Test that a user can submit additional profile information after signup."""
        signup_follow_url = reverse('signup_follow')
        follow_data = {
            'target_weight': 70.0,
            'current_weight': 75.0,
            'height': 180,
            'weekly_physical_activity': 3,
            'gender': 'M',
            'dietary_restriction': 'None',
            'first_name': 'New',
            'birthday': '2000-01-01'
        }
        response = self.client.post(signup_follow_url, json.dumps(follow_data), content_type="application/json")
        self.assertEqual(response.status_code, 200)

        user = User.objects.get(username='testuser')
        self.assertEqual(user.target_weight, 70.0)
        self.assertEqual(user.current_weight, 75.0)
        self.assertEqual(user.height, 180)
        self.assertEqual(user.weekly_physical_activity, 3)
        self.assertEqual(user.gender, 'M')
        self.assertEqual(user.dietary_restriction, 'None')
        self.assertEqual(user.first_name, 'New')
        self.assertEqual(str(user.birthday), '2000-01-01')

    def test_signin_view(self):
        """Test the signin view for authenticating a user."""
        url = reverse('signin')
        data = {
            'username': 'testuser',
            'password': 'password123'
        }
        response = self.client.post(url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_sign_out_view(self):
        """Test the sign out view logs a user out."""
        sign_out_url = reverse('signout')
        response = self.client.post(sign_out_url)
        self.assertEqual(response.status_code, 200)

    def test_get_user_info(self):
        """Test retrieving user information."""
        self.user.first_name = 'Test'
        self.user.gender = 'M'
        self.user.target_weight = 70
        self.user.current_weight = 75
        self.user.height = 180
        self.user.weekly_physical_activity = 5
        self.user.save()

        url = reverse('get_user_info')
        response = self.client.get(url)
        data = json.loads(response.content)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['username'], 'testuser')
        self.assertEqual(data['email'], 'test@example.com')
        self.assertEqual(data['first_name'], 'Test')
        self.assertEqual(data['gender'], 'M')
        self.assertEqual(data['target_weight'], 70)
        self.assertEqual(float(data['current_weight']), 75)
        self.assertEqual(float(data['height']), 180)
        self.assertEqual(data['weekly_physical_activity'], 5)

    def test_change_password(self):
        """Test changing the user's password."""
        url = reverse('change_password')
        data = {'new_password': 'newpassword123'}
        response = self.client.post(url, json.dumps(data), content_type="application/json")
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertTrue(User.objects.filter(email='test@example.com').exists())

    def test_account_deletion(self):
        """Test that deleting a user account removes all associated personal information."""
        url = reverse('change_password')
        data = {'new_password': 'password123'}
        response = self.client.post(url, json.dumps(data), content_type="application/json")

        fridge = Fridge.objects.create(user=self.user)
        ingredient = Ingredient.objects.create(name='Tomato')
        fridge.ingredients.add(ingredient)
        
        recipe = Recipe.objects.create(name='Tomato Salad', preparation='Mix all ingredients.')
        schedule = Schedule.objects.create(user=self.user, meal_type='Dinner', date_and_time=timezone.now())
        schedule.recipes.add(recipe)

        # Delete the user account
        url = reverse('delete_account')
        data = {'password': data.get('new_password')}
        response = self.client.delete(url, json.dumps(data), content_type="application/json")

        # Verify the user and all related data are deleted
        self.assertEqual(response.status_code, 200) # Check error code for successful deletion       
        self.assertFalse(User.objects.filter(username='testuser').exists()) # Check if user is deleted
        self.assertFalse(Fridge.objects.filter(user=self.user).exists()) # Check if fridge is deleted
        self.assertTrue(Ingredient.objects.filter(name='Tomato').exists())  # Check if ingredient still exists
        self.assertTrue(Recipe.objects.filter(name='Tomato Salad').exists())  # Check if recipe still exists
        self.assertFalse(Schedule.objects.filter(user=self.user).exists()) # Check if schedule is deleted

class FridgeIngredientTests(TestCase):
    def setUp(self):
        """Create a user and log them in for testing."""
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password123')
        self.client.login(username='testuser', password='password123')
 
        # Create an Ingredient for testing
        self.ingredient = Ingredient.objects.create(name='Tomato')

        # Create a Fridge associated with the test user
        self.fridge = Fridge.objects.create(user=self.user)

    def test_add_ingredient_to_fridge_and_calories(self):
        """Test adding an ingredient with calorie information to the fridge."""
        url = reverse('add_ingredients_to_fridge')
        data = {'ingredients': [self.ingredient.name]}
        
        response = self.client.post(url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.fridge.ingredients.filter(name=self.ingredient.name).exists())

    def test_view_fridge_contents(self):
        """Test viewing the ingredients in the fridge."""
        self.fridge.ingredients.add(self.ingredient)

        url = reverse('view_fridge_contents')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn(self.ingredient.name, data['ingredients'])

    def test_remove_ingredients_from_fridge(self):
        """Test removing ingredients from the fridge."""
        cucumber = Ingredient.objects.create(name='Cucumber')
        self.fridge.ingredients.add(self.ingredient, cucumber)

        # Remove one ingredient
        url = reverse('remove_ingredients_from_fridge')
        data = {'ingredients': [self.ingredient.name]}
        
        response = self.client.post(url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.fridge.ingredients.filter(name=self.ingredient.name).exists()) # Check Tomato is removed
        self.assertTrue(self.fridge.ingredients.filter(name=cucumber.name).exists()) # Check Cucumber is still there

        # Test removing all ingredients
        data = {'ingredients': []}
        response = self.client.post(url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.fridge.ingredients.exists())  # The fridge should now be empty

class RecipeTests(TestCase):
    def setUp(self):
        """Create a user for the test and ingredients with calorie information."""
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username=self.user.username, password='password123')

        # Complete the health profile
        health_profile_data = {
            'current_weight': 70,
            'target_weight': 75,
            'height': 170,
            'weekly_physical_activity': 3,
            'gender': 'male',
            'dietary_restriction': 'none',
            'birthday': '1990-01-01'
        }
        self.client.post(reverse('signup_follow'), data=health_profile_data, content_type='application/json')
        
        # Now including calories when creating ingredients
        self.ingredient1 = Ingredient.objects.create(
            name='Tomato'
        )

        self.ingredient2 = Ingredient.objects.create(
            name='Cucumber'
        )

    def test_recipe_creation_and_ingredient_association(self):
        """Test creating a recipe and associating it with ingredients including calorie information."""
        self.recipe = Recipe.objects.create(
            name='Salad',
            preparation='Chop ingredients and mix.',
            meal_type='Lunch',
            instructions='Mix all ingredients in a bowl.'
        )
        self.recipe.ingredients.set([self.ingredient1, self.ingredient2])

        # Verify the recipe was created
        self.assertEqual(Recipe.objects.count(), 1)

        # Verify the ingredients are associated with the recipe and have correct calorie information
        self.assertEqual(self.recipe.ingredients.count(), 2)
        self.assertIn(self.ingredient1, self.recipe.ingredients.all())
        self.assertIn(self.ingredient2, self.recipe.ingredients.all())

    def test_log_meal_success(self):
        """Test successfully logging a meal with all details provided."""
        recommended_calories_url = reverse('caloric_intake_recommendation')
        response = self.client.get(recommended_calories_url)
        
        data = json.loads(response.content.decode('utf-8'))
        recommended_calories = data['recommended_calories']
        
        meal_calories = int(recommended_calories) / 4

        url = reverse('log_meal')
        meal_data = {
            'breakfast': meal_calories,
            'lunch': meal_calories,
            'dinner': meal_calories,
            'snacks': meal_calories
        }
        response = self.client.post(url, json.dumps(meal_data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn('You have met your daily calorie goal', response.json()['calorie_status'])

class ScheduleTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username=self.user.username, password='password123')

        self.ingredient1 = Ingredient.objects.create(
            name='Tomato'
        )
        self.ingredient2 = Ingredient.objects.create(
            name='Lettuce'
        )
        self.recipe = Recipe.objects.create(
            name='Salad',
            preparation='Chop ingredients and mix.',
            meal_type='Lunch',
            instructions='Mix all ingredients in a bowl.'
        )

        # Add both ingredients to the recipe
        self.recipe.ingredients.set([self.ingredient1, self.ingredient2])
        self.recipe.save()

    def test_schedule_creation(self):
        schedule_time = timezone.now() + timedelta(days=1)  # Schedule for tomorrow
        schedule = Schedule.objects.create(
            user=self.user,
            date_and_time=schedule_time,
            meal_type='Lunch'
        )
        schedule.recipes.add(self.recipe)
        schedule.save()

        # Verify the schedule was created and associated correctly
        self.assertEqual(Schedule.objects.count(), 1)
        self.assertEqual(schedule.recipes.count(), 1)
        self.assertIn(self.recipe, schedule.recipes.all())
        
        # Verify that the recipe ingredients include the expected ingredients with calories
        recipe_ingredients = list(schedule.recipes.first().ingredients.all())
        self.assertIn(self.ingredient1, recipe_ingredients)
        self.assertIn(self.ingredient2, recipe_ingredients)

    @patch('NutriPapiApp.views.get_current_time')
    def test_meal_reminder_within_one_hour(self, mock_get_current_time):
        """Test receiving a meal reminder within one hour before the scheduled meal time."""

        # Simulate current time being 30 minutes before the meal
        simulated_time = timezone.now().replace(hour=7, minute=30, second=0, microsecond=0, tzinfo=pytz.utc)
        mock_get_current_time.return_value = simulated_time

        # Schedule a meal within the next hour
        schedule_time = simulated_time + timedelta(minutes=30)
        Schedule.objects.create(user=self.user, date_and_time=schedule_time, meal_type='breakfast')

        response = self.client.get(reverse('meal_reminder'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Reminder', response.json()['reminder'])

    @patch('NutriPapiApp.views.get_current_time')
    def test_meal_reminder_outside_one_hour(self, mock_get_current_time):
        """Test not receiving a meal reminder when outside the one-hour window before the scheduled meal time."""

        # Simulate current time being 2 hours before the meal
        simulated_time = timezone.now().replace(hour=10, minute=0, second=0, microsecond=0, tzinfo=pytz.utc)
        mock_get_current_time.return_value = simulated_time

        # Schedule a meal outside the next hour
        schedule_time = simulated_time + timedelta(hours=2)
        Schedule.objects.create(user=self.user, date_and_time=schedule_time, meal_type='lunch')

        response = self.client.get(reverse('meal_reminder'))
        self.assertEqual(response.status_code, 204)

    @patch('NutriPapiApp.views.get_current_time')
    def test_no_meal_scheduled(self, mock_get_current_time):
        """Test not receiving a meal reminder when no meal is scheduled."""
        self.client.login(username=self.user.username, password='password123')

        # Simulate any current time
        simulated_time = timezone.now().replace(hour=10, minute=0, second=0, microsecond=0, tzinfo=pytz.utc)
        mock_get_current_time.return_value = simulated_time

        response = self.client.get(reverse('meal_reminder'))
        self.assertEqual(response.status_code, 204)