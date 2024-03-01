Feature: Daily Calorie Intake Recommendation
  As a NutriPapi user,
  I would like to receive a daily caloric intake recommendation,
  So that I can adjust my diet to meet my weight goals.

  Scenario: Receive Daily Caloric Intake Recommendation (Normal Flow)
    Given the user has logged into the NutriPapi system and entered their attributes,
    When they request a daily caloric intake recommendation,
    Then the system calculates and displays their recommended daily caloric intake.

  Scenario: Request Caloric Intake Recommendation without Completing Profile (Error Flow)
    Given the user has logged into the NutriPapi system but has not completed their health profile,
    When they request a daily caloric intake recommendation without a complete profile,
    Then a "Please complete your health profile" error message is displayed.