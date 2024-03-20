@given(u'the user has logged into the NutriPapi system and navigated to the profile page,')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user has logged into the NutriPapi system and navigated to the profile page,')


@when(u'they select the option to delete their account and confirm their decision by entering their password,')
def step_impl(context):
    raise NotImplementedError(u'STEP: When they select the option to delete their account and confirm their decision by entering their password,')


@then(u'the system permanently deletes their account and all associated personal data, displaying a confirmation message that their account has been successfully deleted.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system permanently deletes their account and all associated personal data, displaying a confirmation message that their account has been successfully deleted.')   


@given(u'the user has selected the option to delete their account in the NutriPapi system,')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user has selected the option to delete their account in the NutriPapi system,')


@when(u'they fail to confirm the account deletion by not entering their password correctly,')
def step_impl(context):
    raise NotImplementedError(u'STEP: When they fail to confirm the account deletion by not entering their password correctly,')


@then(u'the system does not delete their account, displaying an error message such as "Account deletion not confirmed. Please confirm to proceed with account deletion."')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system does not delete their account, displaying an error message such as "Account deletion not confirmed. Please confirm to proceed with account deletion."') 