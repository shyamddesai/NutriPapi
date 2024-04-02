from behave import given, when, then, use_step_matcher
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client
import json

use_step_matcher("re")

@given(u'the user is logged into the NutriPapi system and navigates to the daily log section.')
def step_impl(context):
    context.client = Client()
    User = get_user_model()
    
    context.response = context.test.client.post(reverse('signup'), {
        'username': 'testuser2',
        'email': 'newuser2@testuser.com',
        'password': 'testpassword'
    }, content_type='application/json')

    login_successful = context.client.login(username='testuser2', password='testpassword')
    # print(login_successful)

    context.client.post(reverse('signup_follow'), {
        "target_weight": 75,
        "current_weight": 70.0,
        "height": 170,
        "weekly_physical_activity": 3,
        "gender": "male",
        "dietary_restriction": "none",
        "first_name": "Test",
        "birthday": "1990-01-01"
    }, content_type='application/json')
    # print(context.response.content)
    # assert context.response.status_code == 200

    context.url = reverse('log_meal')

@when(u'the user enters details of a meal that meet the daily calorie goal')
def step_impl(context):
    recommended_calories_url = reverse('caloric_intake_recommendation')
    response = context.test.client.get(recommended_calories_url)
    
    data = json.loads(response.content.decode('utf-8'))
    recommended_calories = data['recommended_calories']
    
    meal_calories = int(recommended_calories) / 4
    # print(recommended_calories)
    # print(meal_calories)
    
    meal_data = {
        'breakfast': meal_calories,
        'lunch': meal_calories,
        'dinner': meal_calories,
        'snacks': meal_calories
    }
    context.response = context.test.client.post(context.url, data=meal_data, content_type='application/json')
    # print(context.response.content)

@then(u'the system should save the meal details')
def step_impl(context):
    assert context.response.status_code == 200

@then(u'display a message that the user has met their daily calorie goal.')
def step_impl(context):
    response_data = json.loads(context.response.content.decode())
    assert 'calorie_status' in response_data and 'You have met your daily calorie goal' in response_data['calorie_status']
    assert 'log_date' in response_data
    assert 'details' in response_data

@when(u'the user enters details of a meal that do not meet the daily calorie goal')
def step_impl(context):
    recommended_calories_url = reverse('caloric_intake_recommendation')
    response = context.test.client.get(recommended_calories_url)
    
    data = json.loads(response.content.decode('utf-8'))
    recommended_calories = data['recommended_calories']
    
    meal_calories = int(recommended_calories - 150) / 4
    # print(recommended_calories)
    # print(meal_calories)
    
    meal_data = {
        'breakfast': meal_calories,
        'lunch': meal_calories,
        'dinner': meal_calories,
        'snacks': meal_calories
    }
    context.response = context.test.client.post(context.url, data=meal_data, content_type='application/json')
    # print(context.response.content)

@then(u'display a message encouraging the user to consume more calories to meet their daily goal.')
def step_impl(context):
    response_data = json.loads(context.response.content.decode())
    assert 'calorie_status' in response_data and 'You have not met your daily calorie goal. You should consider eating more.' in response_data['calorie_status']
    assert 'log_date' in response_data
    assert 'details' in response_data

@when(u'the user enters empty details for a meal')
def step_impl(context):
    context.response = context.test.client.post(context.url, json.dumps({}), content_type='application/json')

@then("the system should prompt the user to complete all required fields.")
def step_impl(context):
    # print(context.response.content)
    # print(context.response.status_code)
    assert context.response.status_code == 400
    response_data = json.loads(context.response.content.decode())
    assert 'error' in response_data and 'All meal fields are required' in response_data['error']