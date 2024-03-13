Feature: Daily Health Reminders
  As a user,
  I want to receive daily reminders to log my meals, drink water, and exercise
  so that I can stay consistent with my health routines.

  Scenario: Receive daily reminders for logging meals, drinking water, and exercising (Normal Flow)
    Given the user has opted in to receive daily health reminders
    When it's the scheduled time for the daily reminder
    Then the system should display a pop-up reminder to log meals, drink water, and exercise.

  Scenario: User opts out of receiving daily health reminders (Alternate Flow)
    Given the user has previously opted in to receive daily health reminders
    When the user chooses to opt out of receiving reminders
    Then the system should disable the daily reminder functionality.

  Scenario: Backend service for pop-up reminder is not available (Error Flow)
    Given the user is expecting to receive a daily health reminder
    When the service for sending the pop-up reminder is down
    Then the system should return an error.