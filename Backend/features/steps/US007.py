@given(u'the user has opted in to receive daily health reminders')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user has opted in to receive daily health reminders')      


@when(u'it\'s the scheduled time for the daily reminder')
def step_impl(context):
    raise NotImplementedError(u'STEP: When it\'s the scheduled time for the daily reminder')


@then(u'the system should display a pop-up reminder to log meals, drink water, and exercise.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system should display a pop-up reminder to log meals, drink water, and exercise.')


@given(u'the user has previously opted in to receive daily health reminders')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user has previously opted in to receive daily health reminders')


@when(u'the user chooses to opt out of receiving reminders')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user chooses to opt out of receiving reminders')


@then(u'the system should disable the daily reminder functionality.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system should disable the daily reminder functionality.')


@given(u'the user is expecting to receive a daily health reminder')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user is expecting to receive a daily health reminder')


@when(u'the service for sending the pop-up reminder is down')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the service for sending the pop-up reminder is down')


@then(u'the system should return an error.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the system should return an error.')