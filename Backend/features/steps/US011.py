from behave import given, when, then, use_step_matcher
from django.urls import reverse
from django.contrib.auth import get_user_model
from NutriPapiApp.models import Schedule, Fridge
import json

use_step_matcher("re")

User = get_user_model()

@given(u'the user has logged into the NutriPapi system and navigates to the account settings page')
def step_impl(context):
    context.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
    context.test.client.login(username='testuser', password='testpassword')

@when(u'the user has selected the option to delete their account and they confirm their decision by entering the correct password')
def step_impl(context):
    data = {'password': 'testpassword'}
    context.response = context.test.client.delete(reverse('delete_account'), json.dumps(data), content_type="application/json")

@then(u'the system permanently deletes their account and all associated personal data, displaying a confirmation message that their account has been successfully deleted.')
def step_impl(context):
    assert context.response.status_code == 200
    response_data = json.loads(context.response.content)
    assert response_data.get('message') == 'Account deleted successfully'
    assert not User.objects.filter(username='testuser').exists()
    assert not Schedule.objects.filter(user=context.user).exists()
    assert not Fridge.objects.filter(user=context.user).exists()

@when(u'the user has selected the option to delete their account and they enter the incorrect password and fail to confirm the account deletion')
def step_impl(context):
    data = {'password': 'wrongpassword'}
    context.response = context.test.client.delete(reverse('delete_account'), json.dumps(data), content_type="application/json")

@then(u'the system does not delete their account, displaying an error message such as "The password entered is incorrect. Please retry to proceed with account deletion."')
def step_impl(context):
    assert context.response.status_code == 400
    response_data = json.loads(context.response.content)
    assert 'error' in response_data
    assert response_data['error'] == 'The password entered is incorrect. Please retry to proceed with account deletion.'