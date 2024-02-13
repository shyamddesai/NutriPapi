from behave import *

use_step_matcher("re")


@given(
    "the user has logged into the NutriPapi system and entered their target weight, current weight, height, and weekly physical activity,")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user has logged into the NutriPapi system and entered their target weight, current weight, height, and weekly physical activity,')


@when("they request a daily caloric intake recommendation,")
def step_impl(context):
    raise NotImplementedError(u'STEP: When they request a daily caloric intake recommendation,')


@then("the system calculates and displays their recommended daily caloric intake\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system calculates and displays their recommended daily caloric intake.')


@given("the user has logged into the NutriPapi system but has not completed their health profile,")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user has logged into the NutriPapi system but has not completed their health profile,')


@then('a "Please complete your health profile" error message is displayed\.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a "Please complete your health profile" error message is displayed.')