from behave import *

use_step_matcher("re")


@given("the user is logged into the NutriPapi system")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is logged into the NutriPapi system')


@when("the user navigates to the health profile management section")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user navigates to the health profile management section')


@step(
    "the user inputs their current weight, target weight, height, weekly physical activity levels, and dietary requirements")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: And the user inputs their current weight, target weight, height, weekly physical activity levels, and dietary requirements')


@then("the system saves the information and acknowledges successful submission")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system saves the information and acknowledges successful submission')


@step(
    "the user modifies their current weight, target weight, height, weekly physical activity levels, or dietary requirements")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: And the user modifies their current weight, target weight, height, weekly physical activity levels, or dietary requirements')


@then("the system updates the information and confirms the changes have been saved")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system updates the information and confirms the changes have been saved')


@step("the user attempts to submit the health profile form with missing or invalid information")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: And the user attempts to submit the health profile form with missing or invalid information')


@then("the system displays error messages for the missing or invalid fields and prompts the user to correct them")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system displays error messages for the missing or invalid fields and prompts the user to correct them')