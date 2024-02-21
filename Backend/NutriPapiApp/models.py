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

    def __str__(self):
        return self.name

class DietaryRestriction(models.Model):
    restriction_type = models.CharField(max_length=255, verbose_name='Restriction Type')
    ingredients = models.ManyToManyField(Ingredient, related_name='dietary_restrictions', verbose_name='Ingredients')

    def __str__(self):
        return self.restriction_type

class User(AbstractUser):
    target_weight = models.FloatField(verbose_name='Target Weight', default=80.0)
    current_weight = models.FloatField(verbose_name='Current Weight', default=80.0)
    dietary_restriction = models.ForeignKey(
        'DietaryRestriction', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name='Dietary Restriction'
    )
    height = models.FloatField(verbose_name='Height in cm', default=160.0)
    weekly_physical_activity = models.IntegerField(
        verbose_name='Weekly Physical Activity in hours',
        validators=[MinValueValidator(0), MaxValueValidator(168)],
        default=0 
    )
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
