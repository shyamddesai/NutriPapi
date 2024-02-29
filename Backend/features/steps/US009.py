from behave import *

use_step_matcher("re")


@given("the user has logged into the NutriPapi system and is creating a new meal plan,")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user has logged into the NutriPapi system and is creating a new meal plan,')


@when("they input meals and specify the meal type \(breakfast, lunch, dinner, or snack\) for each,")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When they input meals and specify the meal type (breakfast, lunch, dinner, or snack) for each,')


@then(
    "the system categorizes the meals accordingly and displays them in the user's daily meal plan under the specified meal type categories\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system categorizes the meals accordingly and displays them in the user\'s daily meal plan under the specified meal type categories.')


@given("the user is reviewing their daily meal plan in the NutriPapi system,")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is reviewing their daily meal plan in the NutriPapi system,')


@when("they choose to edit a meal and change its meal type category \(e\.g\., from lunch to dinner\),")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When they choose to edit a meal and change its meal type category (e.g., from lunch to dinner),')


@then(
    "the system updates the meal's categorization and displays it under the new specified meal type in the daily meal plan\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system updates the meal\'s categorization and displays it under the new specified meal type in the daily meal plan.')


@given("the user is inputting or editing a meal in their NutriPapi meal plan,")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is inputting or editing a meal in their NutriPapi meal plan,')


@when("they forget to select a meal type category or select an invalid category,")
def step_impl(context):
    raise NotImplementedError(u'STEP: When they forget to select a meal type category or select an invalid category,')


@then(
    'the system displays an error message such as "Please select a valid meal type category" and prompts the user to select from the available options \(breakfast, lunch, dinner, snack\)\.')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system displays an error message such as "Please select a valid meal type category" and prompts the user to select from the available options (breakfast, lunch, dinner, snack).')