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
        'breakfast': 'Oatmeal',
        'lunch': 'Salad',
        'dinner': 'Grilled Chicken'
    }
    context.response = context.test.client.post(context.url, json.dumps(meal_data), content_type='application/json')

@then(u'the system should save the meal and display them in the user\'s daily health log.')
def step_impl(context):
    assert context.response.status_code == 200
    response_data = json.loads(context.response.content)
    assert 'message' in response_data and response_data['message'] == 'Meal and exercise details logged successfully'
    assert all(meal in response_data['details'] for meal in ['breakfast', 'lunch', 'dinner'])


@when(u'the user enters empty details for a meal')
def step_impl(context):
    context.response = context.test.client.post(context.url, json.dumps({}), content_type='application/json')

@then("the system should prompt the user to complete all required fields.")
def step_impl(context):
    # print(context.response.content)
    # print(context.response.status_code)
    assert context.response.status_code == 400
    response_data = json.loads(context.response.content.decode())
    assert 'error' in response_data and 'Meal details are required' in response_data['error']