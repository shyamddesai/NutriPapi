from behave import given, when, then
from django.urls import reverse
from NutriPapiApp.models import Ingredient, User
from django.test.client import Client

@given('the user is logged into the NutriPapi system and navigates to the ingredient search section for their meal suggestions.')
def step_impl(context):
     # Create the user and log them in
    context.user = User.objects.create_user(username='testuser', password='testpassword')
    context.client = Client()
    context.client.force_login(context.user)

    # Create an ingredient to ensure the search will find it
    Ingredient.objects.create(name='banana', nutritional_information='Some info', calories=100)

    context.url = reverse('search')

@when('the user searches for an ingredient by name.')
def step_impl(context):
    
    context.response = context.client.get(context.url + '?keyword=banana')

@then('the system should display detailed nutritional information about that ingredient.')
def step_impl(context):
    
    assert 'banana' in context.response.json()['results'][0]['name']

@given('the user is logged into the NutriPapi system and navigates to the ingredient search section.')
def step_impl(context):
    
    context.user = User.objects.create_user(username='testuser2', password='testpassword')
    context.client = Client()
    context.client.force_login(context.user)
    context.url = reverse('search')


@when('the user searches for an ingredient that is not available in the system\'s database.')
def step_impl(context):
    
    context.response = context.client.get(context.url + '?keyword=nonexistentingredient')

@then('the system should display a message indicating that the ingredient is not found.')
def step_impl(context):
    assert context.response.status_code == 200
    assert len(context.response.json()['results']) == 0




