from datetime import timezone
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name='Recipe Name')
    preparation = models.TextField(verbose_name='Recipe Preparation')
    meal_type = models.CharField(max_length=100, verbose_name='Recipe Meal Type')
    instructions = models.TextField(verbose_name='Recipe Instructions')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ingredient Name')
    nutritional_information = models.TextField(verbose_name='Nutritional Information')
    recipes = models.ManyToManyField(Recipe, related_name='ingredients', verbose_name='Recipes')
    calories = models.IntegerField(verbose_name='Calories per Standard Unit', null=True, blank=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    target_weight = models.FloatField(verbose_name='Target Weight', default=80.0)
    current_weight = models.FloatField(verbose_name='Current Weight', default=80.0)
    dietary_restriction = models.CharField(max_length=255, verbose_name='Dietary Restriction', null=True, blank=True)
    height = models.FloatField(verbose_name='Height in cm', default=160.0)
    weekly_physical_activity = models.IntegerField(
        verbose_name='Weekly Physical Activity in hours',
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=0 
    )
    goals = models.CharField(max_length=255, verbose_name='Goals', null=True, blank=True)
    birthday = models.DateField(verbose_name='Birthday', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], verbose_name='Gender', default='M')
    
    def __str__(self):
        return self.username

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedules', verbose_name='User')
    date_and_time = models.DateTimeField(verbose_name='Date and Time')
    meal_type = models.CharField(max_length=100, verbose_name='Meal Type')
    recipes = models.ManyToManyField(Recipe, related_name='schedules', verbose_name='Recipes')

    def __str__(self):
        return f"{self.date_and_time} - {self.meal_type}"
    
class Fridge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='fridge', verbose_name='User')
    ingredients = models.ManyToManyField(Ingredient, related_name='fridges', verbose_name='Ingredients')

    def __str__(self):
        return f"{self.user.username}'s Fridge"    