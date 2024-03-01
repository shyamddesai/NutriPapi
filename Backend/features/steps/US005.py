from behave import given, when, then, use_step_matcher
from django.urls import reverse
from django.contrib.auth import get_user_model
import json

use_step_matcher("re")

@given("the user is logged into the NutriPapi system and the user navigates to the profile settings.")
def step_impl(context):
    User = get_user_model()
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
    context.test.client.login(username='testuser', password='testpassword')
    context.url = reverse('user_info')

@when("the user updates their weight to a new valid value.")
def step_impl(context):
    context.response = context.test.client.post(context.url, json.dumps({
        'current_weight': 75
    }), content_type='application/json')

@then(
    "the system should save the updated weight and recalculate the daily caloric intake recommendations based on the new weight.")
def step_impl(context):
    assert context.response.status_code == 200
    user = get_user_model().objects.get(username='testuser')
    assert user.current_weight == 75, "Current weight was not updated."

@when("the user attempts to update their weight with an invalid value.")
def step_impl(context):
       context.response = context.test.client.post(context.url, json.dumps({
        # 'current_weight': 'invalidWeight'
        'current_weight': -50
    }), content_type='application/json')

@then("the system should display an error message indicating the weight is not valid.")
def step_impl(context):
    assert context.response.status_code == 400
    response_data = json.loads(context.response.content.decode())
    assert 'error' in response_data, "Error message not returned for invalid weight"    

@when("the user enters a weight that is the same as their current weight.")
def step_impl(context):
    user = get_user_model().objects.get(username='testuser')
    context.response = context.test.client.post(context.url, json.dumps({
        'current_weight': user.current_weight
    }), content_type='application/json')

@then(
    "the system should either prompt the user for a different weight or confirm the existing weight without recalculating the daily caloric intake.")
def step_impl(context):
    assert context.response.status_code == 200, "Unexpected status code returned"