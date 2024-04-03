from NutriPapiApp.models import Fridge, Ingredient
from behave import given, when, then
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model
import json


@given(
    u'the user is logged into the NutriPapi system and navigates to the ingredient search section for their meal suggestions.')
def step_impl(context):
    User = get_user_model()
    user = User.objects.create(username='testuser', email='testuser@example.com', password='testpassword')
    context.client = Client()
    context.client.force_login(user)
    context.user = user
    ingredients_info = [
        {'name': 'apple', 'nutritional_information': 'Vitamins: A, C, Calcium'},
        {'name': 'banana', 'nutritional_information': 'Vitamins: B6, C, Potassium'},
        {'name': 'orange', 'nutritional_information': 'Vitamins: C, B9, Potassium'}
    ]
    for item in ingredients_info:
        Ingredient.objects.update_or_create(
            name=item['name'],
            defaults={
                'nutritional_information': item['nutritional_information'],
            }
        )


@when(u'the user searches for an ingredient by name.')
def step_impl(context):
    search_response = context.client.get(reverse('search'), {'keyword': 'apple'})
    context.search_response = search_response


@then(u'the system should display detailed nutritional information about that ingredient.')
def step_impl(context):
    search_result = json.loads(context.search_response.content)
    apple_info = search_result['results'][0]  # Assuming apple is the first result
    assert apple_info['nutritional_information'] == 'Vitamins: A, C, Calcium', "Incorrect nutritional information."


@given(u'the user is logged into the NutriPapi system and navigates to the ingredient search section.')
def step_impl(context):
    User = get_user_model()
    user = User.objects.create(username='testuser', email='testuser@example.com', password='testpassword')
    context.client = Client()
    context.client.force_login(user)
    context.user = user
    ingredients_info = [
        {'name': 'apple', 'nutritional_information': 'Vitamins: A, C, Calcium'},
        {'name': 'banana', 'nutritional_information': 'Vitamins: B6, C, Potassium'},
        {'name': 'orange', 'nutritional_information': 'Vitamins: C, B9, Potassium'}
    ]
    for item in ingredients_info:
        Ingredient.objects.update_or_create(
            name=item['name'],
            defaults={
                'nutritional_information': item['nutritional_information'],
            }
        )


@when(u'the user searches for an ingredient that is not available in the system\'s database.')
def step_impl(context):
    search_response = context.client.get(reverse('search'), {'keyword': 'cucumber'})
    context.search_response = search_response


@then(u'the system should display a message indicating that the ingredient is not found.')
def step_impl(context):
    search_result = json.loads(context.search_response.content)
    assert len(search_result['results']) == 0, "Incorrect number of results returned"


@when("the user enters nothing into the search box for ingredient.")
def step_impl(context):
    search_response = context.client.get(reverse('search'), {'keyword': ''})
    context.search_response = search_response


@then("the system should ask the user to enter the name.")
def step_impl(context):
    search_result = json.loads(context.search_response.content)
    assert len(search_result['results']) == 0, "Incorrect number of results returned"