from behave import *

use_step_matcher("re")


@given("the user is logged into the NutriPapi system and navigates to the ingredient search section\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user is logged into the NutriPapi system and navigates to the ingredient search section.')


@when("the user searches for an ingredient by name\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user searches for an ingredient by name.')


@then("the system should display detailed nutritional information about that ingredient\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system should display detailed nutritional information about that ingredient.')


@when("the user searches for an ingredient that is not available in the system's database\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When the user searches for an ingredient that is not available in the system\'s database.')


@then("the system should display a message indicating that the ingredient is not found\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system should display a message indicating that the ingredient is not found.')


@when("the user enters a vague or incomplete name for an ingredient\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters a vague or incomplete name for an ingredient.')


@then("the system should suggest possible matches or ask the user to provide more specific information\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system should suggest possible matches or ask the user to provide more specific information.')