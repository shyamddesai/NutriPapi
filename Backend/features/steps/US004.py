from NutriPapiApp.models import Fridge, Ingredient
from behave import given, when, then
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model
import json

@given('the user is logged into the NutriPapi system and at the fridge page,')
def step_impl(context):
    User = get_user_model()
    user = User.objects.create(username='testuser', email='testuser@example.com', password='testpassword')
    context.client = Client()
    context.client.force_login(user)
    context.user = user
    # Pre-populate the fridge to ensure there are contents to view
    fridge, _ = Fridge.objects.get_or_create(user=user)
    ingredients = ['apple', 'banana', 'orange']
    for item in ingredients:
        ingredient, _ = Ingredient.objects.get_or_create(name=item)
        fridge.ingredients.add(ingredient)

@when('they view the contents of their fridge,')
def step_impl(context):
    context.response = context.client.get(reverse('view_fridge_contents'))

@then('the system displays all the ingredients currently stored in the fridge.')
def step_impl(context):
    assert context.response.status_code == 200
    response_data = json.loads(context.response.content)
    assert len(response_data['ingredients']) == 3
    for ingredient in ['apple', 'banana', 'orange']:
        assert ingredient in response_data['ingredients']


@when('they add ingredients to their fridge,')
def step_impl(context):
    url = reverse('add_ingredients_to_fridge')
    context.response = context.client.post(url, json.dumps({'ingredients': 'apple,banana,orange'}), content_type='application/json')

@then('those ingredients are stored in the user\'s fridge in the system.')
def step_impl(context):
    assert context.response.status_code == 200
    fridge = Fridge.objects.get(user=context.user)
    ingredients = [ingredient.name for ingredient in fridge.ingredients.all()]
    assert set(ingredients) == {'apple', 'banana', 'orange'}

@when('they attempt to add an empty ingredient list to their fridge,')
def step_impl(context):
    url = reverse('add_ingredients_to_fridge')
    context.response = context.client.post(url, json.dumps({'ingredients': ''}), content_type='application/json')

@then('the system displays an error message indicating that no ingredients were added.')
def step_impl(context):
    assert context.response.status_code == 400
    response_data = json.loads(context.response.content.decode())
    assert 'error' in response_data

@when('they remove one or more ingredients from their fridge,')
def step_impl(context):
    url = reverse('remove_ingredients_from_fridge')
    context.response = context.client.post(url, json.dumps({'ingredients': ['apple']}), content_type='application/json')

@then('those ingredients are no longer listed in the user\'s fridge in the system.')
def step_impl(context):
    assert context.response.status_code == 200
    fridge = Fridge.objects.get(user=context.user)
    ingredients = [ingredient.name for ingredient in fridge.ingredients.all()]
    assert 'apple' not in ingredients


