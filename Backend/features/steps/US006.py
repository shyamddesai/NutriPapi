from behave import given, when, then, use_step_matcher
from django.urls import reverse
from django.contrib.auth import get_user_model
import json

use_step_matcher("re")

@given(u'the user is logged into the NutriPapi system and navigates to the daily log section.')
def step_impl(context):
    User = get_user_model()
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
    context.test.client.login(username='testuser', password='testpassword')
    context.url = reverse('log_meal')

@when(u'the user enters details of a meal')
def step_impl(context):
    meal_data = {
            'meal': {
                'recipe_id': 1,  # Assuming a valid recipe_id for the test
                'meal_type': 'breakfast',
                'portion_size': 1
            }
        }
    context.response = context.test.client.post(context.url, json.dumps(meal_data), content_type='application/json')

@then(u'the system should save the meal and display them in the user\'s daily health log.')
def step_impl(context):
    assert context.response.status_code == 200
    response_data = json.loads(context.response.content)
    assert 'meal' in response_data, "Meal data was not returned"

@when(u'the user enters empty details for a meal')
def step_impl(context):
    context.response = context.test.client.post(context.url, json.dumps({'meal': {}}), content_type='application/json')

@then("the system should prompt the user to complete all required fields.")
def step_impl(context):
    assert context.response.status_code != 200
    response_data = json.loads(context.response.content.decode())
    assert 'error' in response_data
    assert 'Meal details are required' in response_data['error']