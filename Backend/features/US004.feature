Feature: Meal Suggestion Based on Fridge Contents
  As a user, I want to be able to input the ingredients I have in my fridge so that the NutriPapi system can recommend different recipes and I can enjoy diverse and healthy meals.

  Scenario: Receive Meal Suggestions (Normal Flow)
    Given the user is logged into the NutriPapi system and has entered the ingredients available in their fridge,
    When they request meal suggestions,
    Then the system suggests meals that can be prepared using those ingredients, considering the user's dietary preferences.

  Scenario: Request Meal Suggestions with No Ingredients Entered (Error Flow)
    Given the user is logged into the NutriPapi system but has not entered any ingredients available in their fridge,
    When they request meal suggestions,
    Then a "No ingredients entered" error message is displayed.

  Scenario: Inputting invalid ingredients (Error Flow)
    Given the user is logged into the NutriPapi system,
    When the user inputs unrecognizable ingredients,
    Then the system should indicate the ingredients are invalid and ask for re-input.
