from behave import *

use_step_matcher("re")


@given("the user is logged into the NutriPapi system and navigates to the tracking section\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user is logged into the NutriPapi system and navigates to the tracking section.')


@when("the user enters details of a meal and the user enters details of an exercise routine\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When the user enters details of a meal and the user enters details of an exercise routine.')


@then("the system should save the meal and exercise information and display them in the user's daily health log\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system should save the meal and exercise information and display them in the user\'s daily health log.')


@when("the user enters empty details for a meal or an exercise routine\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters empty details for a meal or an exercise routine.')


@then("the system should prompt the user to complete all required fields\.")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system should prompt the user to complete all required fields.')