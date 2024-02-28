Feature: Logging daily meals and exercise routines
  As a user, I want to log my daily meals and exercise routines
  so that I can track my progress towards my health goals over time.

  Scenario: Successfully logging daily meals and exercise routines (Normal Flow)
    Given the user is logged into the NutriPapi system and navigates to the tracking section.
    When the user enters details of a meal and the user enters details of an exercise routine.
    Then the system should save the meal and exercise information and display them in the user's daily health log.

  Scenario: Entering incomplete details for meals or exercise routines (Error Flow)
    Given the user is logged into the NutriPapi system and navigates to the tracking section.
    When the user enters empty details for a meal or an exercise routine.
    Then the system should prompt the user to complete all required fields.
