from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from NutriPapiApp.encryption_utils import encrypt_data, decrypt_data

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
        default=1 
    )
    goals = models.CharField(max_length=255, verbose_name='Goals', null=True, blank=True)
    birthday = models.DateField(verbose_name='Birthday', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], verbose_name='Gender', default='M')

    # Add fields for account lockout
    failed_login_attempts = models.IntegerField(default=0, verbose_name='Failed Login Attempts')
    lockout_until = models.DateTimeField(null=True, blank=True, verbose_name='Lockout Until')
        
    # Add encrypted fields for sensitive data
    encrypted_birthday = models.BinaryField(verbose_name='Encrypted Birthday', null=True, blank=True)
    encrypted_email = models.BinaryField(verbose_name='Encrypted Email', null=True, blank=True)
    encrypted_weight = models.BinaryField(verbose_name='Encrypted Weight', null=True, blank=True)
    encrypted_height = models.BinaryField(verbose_name='Encrypted Height', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.birthday:
            self.encrypted_birthday = encrypt_data(str(self.birthday))
        if self.email:
            self.encrypted_email = encrypt_data(self.email)
        if self.current_weight:
            self.encrypted_weight = encrypt_data(str(self.current_weight))
        if self.height:
            self.encrypted_height = encrypt_data(str(self.height))
        super().save(*args, **kwargs)

    def get_birthday(self):
        return decrypt_data(self.encrypted_birthday) if self.encrypted_birthday else None

    def get_email(self):
        return decrypt_data(self.encrypted_email) if self.encrypted_email else None

    def get_weight(self):
        return decrypt_data(self.encrypted_weight) if self.encrypted_weight else None

    def get_height(self):
        return decrypt_data(self.encrypted_height) if self.encrypted_height else None
    
    def is_locked(self):
        """Check if the user's account is currently locked."""
        return (self.lockout_until and timezone.now() < self.lockout_until) # Returns True if the lockout is still active

    def lock_account(self):
        """Lock the user's account due to repeated failed login attempts."""
        self.lockout_until = timezone.now() + timedelta(minutes=5) # Lock the account for 5 minutes
        self.failed_login_attempts = 0 # Reset the count of failed login attempts
        self.save()

    def reset_failed_attempts(self):
        """Reset the count of failed login attempts."""
        self.failed_login_attempts = 0
        self.lockout_until = None
        self.save()

    def __str__(self):
        return self.username
    
class MealLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs', verbose_name='User')
    date_and_time = models.DateTimeField(auto_now_add=True, verbose_name='Date and Time')
    calories = models.IntegerField(verbose_name='Calories') # Total calories for the meal
    breakfast_calories = models.IntegerField(verbose_name='Calories for Breakfast', null=True, blank=True)
    lunch_calories = models.IntegerField(verbose_name='Calories for Lunch', null=True, blank=True)
    dinner_calories = models.IntegerField(verbose_name='Calories for Dinner', null=True, blank=True)
    snacks_calories = models.IntegerField(verbose_name='Calories for Snacks', null=True, blank=True)


    def __str__(self):
        return f"{self.user.username}'s {self.meal_type} on {self.date_and_time}"

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