Feature: Searching for ingredients to receive nutritional information
  As a health-conscious user,
  I want to search for ingredients by name
  and receive detailed nutritional information about them
  so that I can make informed choices about the ingredients I use in my meals.

  Scenario: Successfully finding nutritional information for an ingredient (Normal Flow)
    Given the user is logged into the NutriPapi system and navigates to the ingredient search section for their meal suggestions.
    When the user searches for an ingredient by name.
    Then the system should display detailed nutritional information about that ingredient.

  Scenario: Searching for an ingredient that is not in the database (Error Flow)
    Given the user is logged into the NutriPapi system and navigates to the ingredient search section.
    When the user searches for an ingredient that is not available in the system's database.
    Then the system should display a message indicating that the ingredient is not found.

 