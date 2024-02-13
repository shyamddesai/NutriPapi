from behave import *

use_step_matcher("re")


@given("the user has logged into the NutriPapi system and navigated to the account settings section,")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user has logged into the NutriPapi system and navigated to the account settings section,')


@when(
    "they select the option to delete their account and confirm their decision by entering their password or responding to a confirmation email,")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When they select the option to delete their account and confirm their decision by entering their password or responding to a confirmation email,')


@then(
    "the system permanently deletes their account and all associated personal data, displaying a confirmation message that their account has been successfully deleted\.")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system permanently deletes their account and all associated personal data, displaying a confirmation message that their account has been successfully deleted.')


@given("the user has selected the option to delete their account in the NutriPapi system,")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user has selected the option to delete their account in the NutriPapi system,')


@when(
    "they fail to confirm the account deletion \(either by not entering their password correctly or not responding to the confirmation email\),")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When they fail to confirm the account deletion (either by not entering their password correctly or not responding to the confirmation email),')


@then(
    'the system does not delete their account, displaying an error message such as "Account deletion not confirmed\. Please confirm to proceed with account deletion\."')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the system does not delete their account, displaying an error message such as "Account deletion not confirmed. Please confirm to proceed with account deletion."')