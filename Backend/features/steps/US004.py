from behave import *

use_step_matcher("re")


@given("the user is logged into the NutriPapi system and has entered the ingredients available in their fridge,")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user is logged into the NutriPapi system and has entered the ingredients available in their fridge,')


@when("they request meal suggestions,")
def step_impl(context):
    raise NotImplementedError(u'STEP: When they request meal suggestions,')


@then(
    "the system suggests meals that can be prepared using those ingredients, considering the user's dietary preferences\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system suggests meals that can be prepared using those ingredients, considering the user\'s dietary preferences.')


@given("the user is logged into the NutriPapi system but has not entered any ingredients available in their fridge,")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user is logged into the NutriPapi system but has not entered any ingredients available in their fridge,')


@then('a "No ingredients entered" error message is displayed\.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a "No ingredients entered" error message is displayed.')


@given("the user is logged into the NutriPapi system,")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is logged into the NutriPapi system,')


@when("the user inputs unrecognizable ingredients,")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user inputs unrecognizable ingredients,')


@then("the system should indicate the ingredients are invalid and ask for re-input\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system should indicate the ingredients are invalid and ask for re-input.')