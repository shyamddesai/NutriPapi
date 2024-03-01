from behave import given, when, then, use_step_matcher
from django.urls import reverse
from django.contrib.auth import get_user_model
import json

use_step_matcher("re")

@given(u'the user is logged into the NutriPapi system and navigates to the daily log section.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is logged into the NutriPapi system and navigates to the daily log section.')

@when(u'the user enters details of a meal')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters details of a meal')

@then(u'the system should save the meal and display them in the user\'s daily health log.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system should save the meal and display them in the user\'s daily health log.')

@when(u'the user enters empty details for a meal')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters empty details for a meal')