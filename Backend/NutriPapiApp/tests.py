from datetime import datetime, timedelta  
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Ingredient, Fridge, Recipe, Schedule
import json

User = get_user_model()

class UserTests(TestCase):

    def test_signup_view(self):
        """Test the signup view for creating a new user."""
        url = reverse('signup')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123'
        }
        response = self.client.post(url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_signin_view(self):
        """Test the signin view for authenticating a user."""
        User.objects.create_user('testuser', 'test@example.com', 'password123')
        url = reverse('signin')
        data = {
            'username': 'testuser',
            'password': 'password123'
        }
        response = self.client.post(url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)



class FridgeIngredientTests(TestCase):

    def setUp(self):
        """Create a user and log them in for testing."""
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password123')
        self.client.login(username='testuser', password='password123')
 
        self.ingredient = Ingredient.objects.create(name='Tomato', nutritional_information='Rich in Vitamin C', calories=18)

    def test_add_ingredient_to_fridge_and_calories(self):
        """Test adding an ingredient with calorie information to the fridge."""
        url = reverse('add_ingredients_to_fridge')
        data = {'ingredients': 'Tomato'}
        response = self.client.post(url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Fridge.objects.filter(user=self.user, ingredients__name='Tomato').exists())

        ingredient_in_fridge = Fridge.objects.get(user=self.user).ingredients.get(name='Tomato')
        self.assertEqual(ingredient_in_fridge.calories, 18)

class UserInfoUpdateTests(TestCase):

    def setUp(self):
        """Create a user and log them in for testing."""
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password123')
        self.client.login(username='testuser', password='password123')

    def test_user_info_update(self):
        """Test updating user information."""
        url = reverse('user_info')
        data = {
            'target_weight': 70,
            'current_weight': 75,
            'height': 180,
            'weekly_physical_activity': 5,
            'gender': 'M'
        }
        response = self.client.post(url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.target_weight, 70)
        self.assertEqual(updated_user.current_weight, 75)
        self.assertEqual(updated_user.height, 180)
        self.assertEqual(updated_user.weekly_physical_activity, 5)
        self.assertEqual(updated_user.gender, 'M')

class RecipeTests(TestCase):

    def setUp(self):
        """Create a user for the test and ingredients with calorie information."""
        self.user = User.objects.create_user(username='testuser', password='password123')
        # Now including calories when creating ingredients
        self.ingredient1 = Ingredient.objects.create(
            name='Tomato', 
            nutritional_information='Rich in Vitamin C', 
            calories=18  # Assuming 18 calories per standard amount (e.g., per 100g)
        )
        self.ingredient2 = Ingredient.objects.create(
            name='Cucumber', 
            nutritional_information='Rich in Vitamin K', 
            calories=16  # Assuming 16 calories per standard amount
        )

    def test_recipe_creation_and_ingredient_association(self):
        """Test creating a recipe and associating it with ingredients including calorie information."""
        recipe = Recipe.objects.create(
            name='Salad',
            preparation='Chop ingredients and mix.',
            meal_type='Lunch',
            instructions='Mix all ingredients in a bowl.'
        )
        recipe.ingredients.add(self.ingredient1, self.ingredient2)
        recipe.save()

        # Verify the recipe was created
        self.assertEqual(Recipe.objects.count(), 1)
        # Verify the ingredients are associated with the recipe and have correct calorie information
        self.assertEqual(recipe.ingredients.count(), 2)
        self.assertIn(self.ingredient1, recipe.ingredients.all())
        self.assertIn(self.ingredient2, recipe.ingredients.all())
        self.assertEqual(self.ingredient1.calories, 18)
        self.assertEqual(self.ingredient2.calories, 16)

class ScheduleTests(TestCase):

    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.ingredient1 = Ingredient.objects.create(
            name='Tomato', 
            nutritional_information='Vitamin C', 
            calories=22  
        )
        self.ingredient2 = Ingredient.objects.create(
            name='Lettuce', 
            nutritional_information='Rich in vitamins A, C, and K', 
            calories=5  # Example calorie count
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
        # Create a schedule for a meal
        schedule_time = datetime.now() + timedelta(days=1)  # Schedule for tomorrow
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
        # Optionally, verify that the recipe ingredients include the expected ingredients with calories
        recipe_ingredients = list(schedule.recipes.first().ingredients.all())
        self.assertIn(self.ingredient1, recipe_ingredients)
        self.assertIn(self.ingredient2, recipe_ingredients)
        self.assertEqual(self.ingredient1.calories, 22)
        self.assertEqual(self.ingredient2.calories, 5)




