from behave import given, when, then, use_step_matcher
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime, time, timedelta
from NutriPapiApp.models import User, Schedule
from unittest.mock import patch
import json
import pytz

use_step_matcher("re")

MEAL_TIMES = {
    'breakfast': time(8, 0),
    'lunch': datetime.time(12, 0),
    'dinner': datetime.time(18, 0)
}

@given(u'the user is logged into the NutriPapi system and navigates to the meals section')
def step_impl(context):
    User = get_user_model()
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
    context.test.client.login(username='testuser', password='testpassword')
    context.url = reverse('meal_reminder')

@when(u'a meal is scheduled within the next one hour')
def step_impl(context):
    user = User.objects.get(username='testuser')
    context.meal_type = 'breakfast'

    utc_now = datetime.now(pytz.utc)
    simulated_time = utc_now.replace(hour=7, minute=30, second=0, microsecond=0) # Simulated 7:30am right now
    print("Simulated time:", simulated_time)

    scheduled_meal_time = simulated_time + timedelta(minutes=30) # Breakfast at 8am
    Schedule.objects.create(user=user, meal_type=context.meal_type, date_and_time=scheduled_meal_time)
    print("Scheduled meal time:", scheduled_meal_time)

    with patch('NutriPapiApp.views.get_current_time', return_value=simulated_time):
        context.response = context.test.client.get(context.url)
        print("Response content:", context.response.content)
        print("Response status code:", context.response.status_code)

    schedules = Schedule.objects.all()
    print("All schedules:", schedules)

@then(u'the system should display a reminder message on the page for the upcoming meal.')
def step_impl(context):
    meal_type = getattr(context, 'meal_type', 'none')
    print("Meal type:", meal_type)

    assert context.response.status_code == 200, "Expected status code 200, but got {context.response.status_code}"
    response_data = json.loads(context.response.content.decode())
    print("Response data:", response_data)

    assert 'reminder' in response_data, "Expected a reminder in the response"
    expected_reminder_message = "Reminder, get your ingredients ready for " + meal_type + "!"
    assert response_data['reminder'] == expected_reminder_message, f"Expected reminder message to be '{expected_reminder_message}', got '{response_data['reminder']}'"
    

@given(u'the user is logged into the NutriPapi system and navigates to the meal section outside of scheduled meal reminder times')
def step_impl(context):
    User = get_user_model()
    user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
    context.test.client.login(username='testuser', password='testpassword')
    context.url = reverse('meal_reminder')

    # Set a time outside of scheduled meal times
    context.current_time = datetime.combine(datetime.today(), time(23, 30))

@when(u'the user checks the dashboard or meal log section')
def step_impl(context):
     context.response = context.test.client.get(context.url, follow=True)

@then(u'the system should not display any reminder message for meal preparation.')
def step_impl(context):
    assert 200 <= context.response.status_code < 300, f"Unexpected status code: {context.response.status_code}"

    # Check if the response has content before trying to load JSON
    if context.response.content:
        response_data = json.loads(context.response.content)
        assert 'reminder' not in response_data, "Reminder message was unexpectedly found in the response."
    else:
        print("No content in response, passing test")
        pass


@when(u'there are no meal suggestions available')
def step_impl(context):
    # Ensure the Schedule table does not have entries for the current user
    user = User.objects.get(username='testuser')
    Schedule.objects.filter(user=user).delete()

    # Attempt to retrieve meal suggestions
    context.url = reverse('meal_reminder')
    context.response = context.test.client.get(context.url, follow=True)

@then(u'the system should inform the user that no reminders can be provided')
def step_impl(context):
    assert context.response.status_code == 204, f"Expected status code 204, got {context.response.status_code}"
    assert not context.response.content, "Expected no content in the response body"