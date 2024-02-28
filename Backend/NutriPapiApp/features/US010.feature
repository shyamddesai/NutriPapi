Feature: Diverse Recipe Recommendations in the NutriPapi System
  As a user who enjoys culinary diversity,
  I want the NutriPapi system to recommend a variety of recipes for different meals each day
  and ensure that the same meal is not repeated within a two-week period unless I specifically request it.

  Scenario: Successfully recommending diverse recipes (Normal Flow)
    Given the user accesses the meal recommendation feature on the NutriPapi system.
    When the system generates meal recommendations for the day.
    Then it should recommend a variety of recipes for different meals that have not been recommended to the user in the past two weeks.

  Scenario: Preventing repeated recipes without specific request (Error Flow)
    Given the system has recommended a specific recipe to the user within the last two weeks.
    When the system generates new meal recommendations for the day.
    Then it should not include any recipes that have been recommended within the past two weeks unless the user has specifically requested a repeat of those recipes.

  Scenario: User requests a repeated recipe not recognized by the system (Error Flow)
    Given the user wants to request a repeat of a recipe recommended within the last two weeks but the system does not recognize it as recently recommended.
    When the user tries to select the recipe for a repeat.
    Then the system should allow the user to manually search for and select the recipe to be repeated, overriding the two-week diversity rule.
