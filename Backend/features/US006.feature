Feature: Logging daily meals
  As a user, I want to log my daily meals
  so that I can track my progress towards my health goals over time.

  Scenario: Successfully logging daily meals (Normal Flow)
    Given the user is logged into the NutriPapi system and navigates to the daily log section.
    When the user enters details of a meal
    Then the system should save the meal and display them in the user's daily health log.

  Scenario: Entering incomplete details for meals or exercise routines (Error Flow)
    Given the user is logged into the NutriPapi system and navigates to the daily log section.
    When the user enters empty details for a meal
    Then the system should prompt the user to complete all required fields.