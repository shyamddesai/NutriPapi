from behave import *

use_step_matcher("re")


@given("the visitor is on the NutriPapi account creation page,")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the visitor is on the NutriPapi account creation page,')


@when("they submit their personal details along with a chosen username and password,")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When they submit their personal details along with a chosen username and password,')


@then("their user account is created, and they are logged into the NutriPapi system\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then their user account is created, and they are logged into the NutriPapi system.')


@when("they attempt to create an account using an email address that is already associated with an existing account,")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When they attempt to create an account using an email address that is already associated with an existing account,')


@then('a "Email already in use" error message is displayed\.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a "Email already in use" error message is displayed.')


@when("they attempt to submit the account creation form without filling out all mandatory fields,")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When they attempt to submit the account creation form without filling out all mandatory fields,')


@then('an "All fields are required" error message is displayed\.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then an "All fields are required" error message is displayed.')