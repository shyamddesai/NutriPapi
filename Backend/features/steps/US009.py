@given(u'the user is logged into the NutriPapi system and navigates to the ingredient search section for their meal suggestions.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is logged into the NutriPapi system and navigates to the ingredient search section for their meal suggestions.')


@when(u'the user searches for an ingredient by name.')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user searches for an ingredient by name.')


@then(u'the system should display detailed nutritional information about that ingredient.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system should display detailed nutritional information about that ingredient.')


@given(u'the user is logged into the NutriPapi system and navigates to the ingredient search section.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is logged into the NutriPapi system and navigates to the ingredient search section.')


@when(u'the user searches for an ingredient that is not available in the system\'s database.')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user searches for an ingredient that is not available in the system\'s database.')


@then(u'the system should display a message indicating that the ingredient is not found.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system should display a message indicating that the ingredient is not found.')


@when(u'the user enters a vague or incomplete name for an ingredient.')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters a vague or incomplete name for an ingredient.')


@then(u'the system should ask the user to provide more specific information.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system should ask the user to provide more specific information.')