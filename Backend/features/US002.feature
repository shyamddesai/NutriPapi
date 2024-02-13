Feature: Health Profile Management

  As a user, I want to input my current weight, target weight, height, weekly physical activity levels, and dietary requirements so that the system can provide me with tailored suggestions on achieving my health goals.

  Scenario: Inputting Health Profile Information (Normal Flow)
    Given the user is logged into the NutriPapi system
    When the user navigates to the health profile management section
    And the user inputs their current weight, target weight, height, weekly physical activity levels, and dietary requirements
    Then the system saves the information and acknowledges successful submission

  Scenario: Editing Health Profile Information (Alternate Flow)
    Given the user is logged into the NutriPapi system
    When the user navigates to the health profile management section
    And the user modifies their current weight, target weight, height, weekly physical activity levels, or dietary requirements
    Then the system updates the information and confirms the changes have been saved

  Scenario: Missing or Invalid Information (Error Flow)
    Given the user is logged into the NutriPapi system
    When the user navigates to the health profile management section
    And the user attempts to submit the health profile form with missing or invalid information
    Then the system displays error messages for the missing or invalid fields and prompts the user to correct them
