from behave import given, when, then, use_step_matcher
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from django.test import Client
from NutriPapiApp.models import User
from NutriPapiApp.encryption_utils  import encrypt_data
from django.utils import timezone
import json

use_step_matcher("re")

@given(u'an user navigates to the registration page of the NutriPapi system')
def step_impl(context):
    context.client = Client()

@when(u'they attempt to register with valid credentials')
def step_impl(context):
    context.url = reverse('signup')
    context.response = context.test.client.post(context.url, {
        'username': 'testuser1',
        'email': 'newuser1@testuser.com',
        'password': 'testpassword'
    }, content_type='application/json')

    context.client.login(username='testuser1', password='testpassword')
    
    # Complete the user registration process so the get_user_info endpoint can be accessed
    user_data = {
        'target_weight': 75.0,
        'current_weight': 70.0,
        'dietary_restriction': 'vegetarian',
        'height': 170,
        'weekly_physical_activity': 3,
        'birthday': '1990-01-01',
        'gender': 'male'
    }
    context.client.post(reverse('signup_follow'), data=user_data, content_type='application/json')

@then(u'the system employs encrypted passwords for secure authentication to safeguard against unauthorized access')
def step_impl(context):
    user = User.objects.get(username='testuser1')
    original_password = 'testpassword'

    # First, let's compare the original password with the stored password using Django's check_password() function which decrypts the stored password
    assert check_password(original_password, user.password), "Stored password doesn't match the original password"

    # Now, let's retrieve the user's information (which includes the user's encrypted password) using the get_user_info endpoint
    get_info_url = reverse('get_user_info')
    get_info_response = context.client.get(get_info_url)
    assert get_info_response.status_code == 200, "Failed to retrieve user info"

    user_info = get_info_response.json()
    retrieved_password = user_info.get('password', None)

    # Compare the retrieved encrypted password with the original non-encrypted password just to be sure
    assert retrieved_password is not None, "Password not found in user info"
    assert retrieved_password != original_password, "Stored password matches the original password"

@given(u'a user inputs or updates their personal health information in the NutriPapi system')
def step_impl(context):
    context.user_data = {
        'current_weight': 70,
        'target_weight': 75,
        'height': 170
    }

@when(u'this data is stored or transmitted by the NutriPapi system')
def step_impl(context):
    # Simulate storing or transmitting of user data
    context.encrypted_data = {}
    for key, value in context.user_data.items():
        context.encrypted_data[key] = encrypt_data(str(value))

@then(u'all sensitive user data is encrypted using industry-standard encryption protocols to ensure that it remains confidential and secure against unauthorized access')
def step_impl(context):
    # Check if all sensitive user data is encrypted
    assert all(isinstance(value, bytes) for value in context.encrypted_data.values()), "Expected all sensitive user data to be encrypted"
    assert len(context.encrypted_data) == len(context.user_data), "Expected encrypted data to have the same number of fields as user data"

@given('repeated failed login attempts on a user\'s account')
def create_user_with_failed_login_attempts(context):
    context.client = Client()
    context.response = context.test.client.post(reverse('signup'), {
        'username': 'testuser',
        'email': 'newuser@testuser.com',
        'password': 'testpassword'
    }, content_type='application/json')

    context.user = User.objects.get(username='testuser')
    context.user.failed_login_attempts = 5
    context.user.save()

@when('the system detects these unauthorized access attempts')
def simulate_unauthorized_access_attempts(context):
    context.response = context.test.client.post(reverse('signin'), data=json.dumps({'username': 'testuser', 'password': 'invalidpassword'}), content_type='application/json')

@then('it temporarily locks the account to prevent further unauthorized access.')
def test_account_temporary_lock(context):
    user = User.objects.get(username='testuser')
    assert user.is_locked(), "User account is not locked"

    lockout_duration = (user.lockout_until - timezone.now()).total_seconds() // 60
    assert lockout_duration >= 4 and lockout_duration <= 6, "Lockout duration is not within expected range"
    
    assert context.response.status_code == 403, "Response status code is not 403"
    assert 'Too many failed login attempts. Your account has been locked for 5 minutes.' in context.response.content.decode(), "Error message doesn't match"

    context.response = context.test.client.post(reverse('signin'), data=json.dumps({'username': 'testuser', 'password': 'invalidpassword'}), content_type='application/json')
    assert 'Your account is temporarily locked. Please try again in ' + str(int(lockout_duration)) + ' minutes.' in context.response.content.decode(), "Error message doesn't match"