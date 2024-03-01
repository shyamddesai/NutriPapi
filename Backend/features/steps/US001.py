
# features/steps/user_creation_steps.py

from behave import given, when, then
from django.urls import reverse
from NutriPapiApp.models import User  # Adjust the import path based on your app name

from django.contrib.auth import get_user_model

@given('the visitor is on the NutriPapi account creation page')
def step_impl(context):
    context.url = reverse('signup')

@when('they submit their personal details along with a chosen username and password')
def step_impl(context):
    # Use context.test.client to maintain session state
    context.response = context.test.client.post(context.url, {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'password123'
    }, content_type='application/json')

@then('their user account is created, and they are logged into the NutriPapi system')
def step_impl(context):
    # First, check that the response indicates success
    assert context.response.status_code == 201, f"Expected HTTP 201, got {context.response.status_code}"
    
    # Now, check if the user is created with the correct attributes
    User = get_user_model()
    try:
        user = User.objects.get(username='newuser')
        assert user is not None, "User was not created."
        assert user.username == 'newuser', "Username does not match."
        assert user.email == 'newuser@example.com', "Email does not match."
    except User.DoesNotExist:
        assert False, "User does not exist."
    
    # Check if the user is logged in by verifying if their session has been established
    assert '_auth_user_id' in context.test.client.session, "User is not logged in."


@when('they attempt to create an account using an email address that is already associated with an existing account')
def step_impl(context):
    # Creating an initial user
    User.objects.create_user('existinguser', 'existing@example.com', 'password123')
    # Attempting to create another user with the same email
    context.response = context.test.client.post(context.url, ({
        'username': 'testuser',
        'email': 'existing@example.com',
        'password': 'password123'
    }), content_type='application/json')

@then('a "Email already in use" error message is displayed')
def step_impl(context):
    context.test.assertIn('Email already in use', context.response.content.decode())

@when('they attempt to submit the account creation form without filling out all mandatory fields')
def step_impl(context):
    context.response = context.test.client.post(context.url, ({
        'username': '',  # Leave out necessary fields
        'email': 'test@example.com',
        'password': 'password123'
    }), content_type='application/json')

@then('an "All fields are required" error message is displayed')
def step_impl(context):
    context.test.assertIn('All fields are required', context.response.content.decode())
