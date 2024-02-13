from behave import *

use_step_matcher("re")


@given("the user is logged into the NutriPapi system and has opted in for daily reminders\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user is logged into the NutriPapi system and has opted in for daily reminders.')


@when("the system reaches the designated reminder times\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the system reaches the designated reminder times.')


@then("the user should receive reminders to log meals, drink water, and exercise\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user should receive reminders to log meals, drink water, and exercise.')


@given("the user is logged into the NutriPapi system and navigates to the reminder settings\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user is logged into the NutriPapi system and navigates to the reminder settings.')


@when("the user opts out of specific reminders such as for logging meals, drinking water, or exercising\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When the user opts out of specific reminders such as for logging meals, drinking water, or exercising.')


@then("the system should update the preferences and not send the opted-out reminders to the user\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system should update the preferences and not send the opted-out reminders to the user.')


@given("the user is logged into the NutriPapi system but has not opted in for any reminders\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user is logged into the NutriPapi system but has not opted in for any reminders.')


@then("the user should not receive any reminders\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user should not receive any reminders.')