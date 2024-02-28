Feature: Updating User Weight in the NutriPapi System
  As a user who may have lost or gained weight,
  I want to update my weight in the NutriPapi system
  so that it can adjust my daily caloric intake recommendations accordingly.

  Scenario: Successfully updating weight (Normal Flow)
    Given the user is logged into the NutriPapi system and the user navigates to the profile settings.
    When the user updates their weight to a new valid value.
    Then the system should save the updated weight and recalculate the daily caloric intake recommendations based on the new weight.

  Scenario: Entering an invalid weight (Error Flow)
    Given the user is logged into the NutriPapi system and the user navigates to the profile settings.
    When the user attempts to update their weight with an invalid value.
    Then the system should display an error message indicating the weight is not valid.

  Scenario: Entering a weight that is the same as the current weight (Error Flow)
    Given the user is logged into the NutriPapi system and the user navigates to the profile settings.
    When the user enters a weight that is the same as their current weight.
    Then the system should either prompt the user for a different weight or confirm the existing weight without recalculating the daily caloric intake.
