from behave import given, when, then, use_step_matcher
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model

import json

use_step_matcher("re")

@given(u'the user has logged into the NutriPapi system and entered their attributes,')
def step_impl(context):
    context.client = Client()
    User = get_user_model()

    user = User.objects.create_user('user', 'user@example.com', 'password')
    context.client.login(username='user', password='password')

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


@when(u'they request a daily caloric intake recommendation,')
def step_impl(context):
    context.response = context.client.get(reverse('caloric_intake_recommendation'))

@then(u'the system calculates and displays their recommended daily caloric intake.')
def step_impl(context):
    assert context.response.status_code == 200
    response_data = json.loads(context.response.content)
    assert 'recommended_calories' in response_data

@given('the user has logged into the NutriPapi system but has not completed their health profile,')
def step_impl(context):
    context.client = Client()
    User = get_user_model()

    user = User.objects.create_user('user2', 'user2@example.com', 'password')
    context.client.login(username='user2', password='password')

@when(u'they request a daily caloric intake recommendation without a complete profile,')
def step_impl(context):
    context.response = context.client.get(reverse('caloric_intake_recommendation'))

@then(u'a "Please complete your health profile" error message is displayed.')
def step_impl(context):
    assert context.response.status_code == 400
    response_data = json.loads(context.response.content)
    assert response_data.get('error') == 'Please complete your health profile'