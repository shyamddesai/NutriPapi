Feature: Managing Fridge Contents
  As a NutriPapi user, 
  I want to be able to input and manage the ingredients I have in my fridge,
  so that I can keep track of what I have available.  

Scenario: Adding Ingredients to the Fridge (Normal Flow)
  Given the user is logged into the NutriPapi system and at the fridge page,
  When they add ingredients to their fridge,
  Then those ingredients are stored in the user's fridge in the system.

Scenario: Viewing Ingredients in the Fridge
  Given the user is logged into the NutriPapi system and at the fridge page,
  When they view the contents of their fridge,
  Then the system displays all the ingredients currently stored in the fridge.

Scenario: Adding No Ingredients (Error Flow)
  Given the user is logged into the NutriPapi system and at the fridge page,
  When they attempt to add an empty ingredient list to their fridge,
  Then the system displays an error message indicating that no ingredients were added.

Scenario: Removing Ingredients from the Fridge
  Given the user is logged into the NutriPapi system and at the fridge page,
  When they remove one or more ingredients from their fridge,
  Then those ingredients are no longer listed in the user's fridge in the system.