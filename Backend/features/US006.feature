Feature: Logging daily meals
  As a user, I want to log my daily meals
  so that I can track my progress towards my health goals over time.

  Scenario: Successfully logging daily meals and meeting calorie goal (Normal Flow)
    Given the user is logged into the NutriPapi system and navigates to the daily log section.
    When the user enters details of a meal that meet the daily calorie goal
    Then the system should save the meal details
    And display a message that the user has met their daily calorie goal.

  Scenario: Successfully logging daily meals but not meeting calorie goal (Alternate Flow)
    Given the user is logged into the NutriPapi system and navigates to the daily log section.
    When the user enters details of a meal that do not meet the daily calorie goal
    Then the system should save the meal details
    And display a message encouraging the user to consume more calories to meet their daily goal.

  Scenario: Entering incomplete details for meals or exercise routines (Error Flow)
    Given the user is logged into the NutriPapi system and navigates to the daily log section.
    When the user enters empty details for a meal
    Then the system should prompt the user to complete all required fields.