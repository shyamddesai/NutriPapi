from behave import *

use_step_matcher("re")


@given("the user is logged into the NutriPapi system and the user navigates to the profile settings\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user is logged into the NutriPapi system and the user navigates to the profile settings.')


@when("the user updates their weight to a new valid value\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user updates their weight to a new valid value.')


@then(
    "the system should save the updated weight and recalculate the daily caloric intake recommendations based on the new weight\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system should save the updated weight and recalculate the daily caloric intake recommendations based on the new weight.')


@when("the user attempts to update their weight with an invalid value\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user attempts to update their weight with an invalid value.')


@then("the system should display an error message indicating the weight is not valid\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system should display an error message indicating the weight is not valid.')


@when("the user enters a weight that is the same as their current weight\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters a weight that is the same as their current weight.')


@then(
    "the system should either prompt the user for a different weight or confirm the existing weight without recalculating the daily caloric intake\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system should either prompt the user for a different weight or confirm the existing weight without recalculating the daily caloric intake.')