from behave import *

use_step_matcher("re")


@given("the user accesses the meal recommendation feature on the NutriPapi system\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user accesses the meal recommendation feature on the NutriPapi system.')


@when("the system generates meal recommendations for the day\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the system generates meal recommendations for the day.')


@then(
    "it should recommend a variety of recipes for different meals that have not been recommended to the user in the past two weeks\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then it should recommend a variety of recipes for different meals that have not been recommended to the user in the past two weeks.')


@given("the user has received a specific recipe recommendation within the past two weeks and requests it again\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user has received a specific recipe recommendation within the past two weeks and requests it again.')


@when("the user selects an option to repeat a previously recommended recipe\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user selects an option to repeat a previously recommended recipe.')


@then("the system should include that recipe in the day's meal recommendations despite the two-week diversity rule\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system should include that recipe in the day\'s meal recommendations despite the two-week diversity rule.')


@given("the system has recommended a specific recipe to the user within the last two weeks\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the system has recommended a specific recipe to the user within the last two weeks.')


@when("the system generates new meal recommendations for the day\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the system generates new meal recommendations for the day.')


@then(
    "it should not include any recipes that have been recommended within the past two weeks unless the user has specifically requested a repeat of those recipes\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then it should not include any recipes that have been recommended within the past two weeks unless the user has specifically requested a repeat of those recipes.')


@given(
    "the user wants to request a repeat of a recipe recommended within the last two weeks but the system does not recognize it as recently recommended\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user wants to request a repeat of a recipe recommended within the last two weeks but the system does not recognize it as recently recommended.')


@when("the user tries to select the recipe for a repeat\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user tries to select the recipe for a repeat.')


@then(
    "the system should allow the user to manually search for and select the recipe to be repeated, overriding the two-week diversity rule\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system should allow the user to manually search for and select the recipe to be repeated, overriding the two-week diversity rule.')