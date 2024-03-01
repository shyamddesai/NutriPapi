from behave import given, when, then, use_step_matcher
from django.urls import reverse
from django.contrib.auth import get_user_model
import json

use_step_matcher("re")

@given('the user is logged into the NutriPapi system')
def step_user_logged_in(context):
    User = get_user_model()
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
    context.test.client.login(username='testuser', password='testpassword')

@when('the user navigates to the health information section')
def step_navigate_health_section(context):
    context.url = reverse('user_info')  # Adjust the URL name as needed

@when('the user inputs their current weight, target weight, height, weekly physical activity levels, gender, and dietary requirements')
def step_input_health_info(context):
    context.response = context.test.client.post(context.url, json.dumps({
        'current_weight': 70,
        'target_weight': 65,
        'height': 175,
        'weekly_physical_activity': 3,
        'gender': 'M',
        'dietary_restriction': 'Vegetarian'
    }), content_type='application/json')

@then('the system saves the information and acknowledges successful submission')
def step_verify_info_saved(context):
    assert context.response.status_code == 200

# Adding steps for editing health profile information scenario
@when('the user modifies their current weight, target weight, height, weekly physical activity levels, gender, or dietary requirements')
def step_modify_health_info(context):
    modified_data = {
        'current_weight': 75,
        'target_weight': 70,
        'height': 180,
        'weekly_physical_activity': 5,
        'gender': 'F',
        'dietary_restriction': 'Vegan'
    }
    context.response = context.test.client.post(context.url, json.dumps(modified_data), content_type='application/json')

@then('the system updates the information and confirms the changes have been saved')
def step_verify_info_updated(context):
    assert context.response.status_code == 200
    user = get_user_model().objects.get(username='testuser')
    assert user.current_weight == 75, "Current weight was not updated."
    assert user.target_weight == 70, "Target weight was not updated."
    assert user.height == 180, "Height was not updated."
    assert user.weekly_physical_activity == 5, "Weekly physical activity level was not updated."
    assert user.gender == 'F', "Gender was not updated."
    # Add checks for dietary restrictions if applicable


@when('the user attempts to submit the health profile form with missing or invalid information')
def step_submit_invalid_health_info(context):
    # Example of missing information: omitting 'current_weight'
    # Example of invalid information: providing a string for 'height' instead of a number
    invalid_data = {
        'current_weight': '',  # Missing information
        'target_weight': 60,
        'height': 'not_a_number',  # Invalid information
        'weekly_physical_activity': 2,
        'gender': 'M',
        'dietary_restriction': 'Vegetarian'
    }
    context.response = context.test.client.post(context.url, json.dumps(invalid_data), content_type='application/json')

@then('the system displays error messages for the missing or invalid fields and prompts the user to correct them')
def step_verify_error_messages(context):
    assert context.response.status_code != 200, "Expected error status code, got 200"
    response_data = json.loads(context.response.content.decode())
    assert 'error' in response_data, "No error message in response"
    # Check for specific error messages (the exact key and message might vary based on your implementation)
    assert 'current_weight' in response_data['error'], "No error for missing current weight"
    
    