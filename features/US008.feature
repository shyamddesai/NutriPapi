Feature: Receiving daily reminders for health routines
  As a user, I want to receive daily reminders to log my meals, drink water, and exercise
  so that I can stay consistent with my health routines.

  Scenario: Receiving all daily reminders (Normal Flow)
    Given the user is logged into the NutriPapi system and has opted in for daily reminders.
    When the system reaches the designated reminder times.
    Then the user should receive reminders to log meals, drink water, and exercise.

  Scenario: Opting out of specific reminders (Alternate Flow)
    Given the user is logged into the NutriPapi system and navigates to the reminder settings.
    When the user opts out of specific reminders such as for logging meals, drinking water, or exercising.
    Then the system should update the preferences and not send the opted-out reminders to the user.

  Scenario: Not receiving reminders when not opted in (Error Flow)
    Given the user is logged into the NutriPapi system but has not opted in for any reminders.
    When the system reaches the designated reminder times.
    Then the user should not receive any reminders.
