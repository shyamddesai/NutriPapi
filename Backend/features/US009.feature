Feature: Meal Plan Categorization
  As a NutriPapi user,
  I want the system to categorize my meal plans into breakfast, lunch, dinner, and snacks
  so that I can have a structured and balanced daily eating schedule.

  Scenario: Meal Plan Categorization upon Creation (Normal Flow)
    Given the user has logged into the NutriPapi system and is creating a new meal plan,
    When they input meals and specify the meal type (breakfast, lunch, dinner, or snack) for each,
    Then the system categorizes the meals accordingly and displays them in the user's daily meal plan under the specified meal type categories.

  Scenario: Editing Meal Plan Categories (Alternate Flow)
    Given the user is reviewing their daily meal plan in the NutriPapi system,
    When they choose to edit a meal and change its meal type category (e.g., from lunch to dinner),
    Then the system updates the meal's categorization and displays it under the new specified meal type in the daily meal plan.

  Scenario: Categorization Error Due to Incorrect Input (Error Flow)
    Given the user is inputting or editing a meal in their NutriPapi meal plan,
    When they forget to select a meal type category or select an invalid category,
    Then the system displays an error message such as "Please select a valid meal type category" and prompts the user to select from the available options (breakfast, lunch, dinner, snack).
