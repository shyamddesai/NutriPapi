Feature: User Account Creation
  As a user, I want to create an account on the NutriPapi system so that I can get access to its functionalities

  Scenario: Create a New User Account (Normal Flow)
    Given the visitor is on the NutriPapi account creation page
    When they submit their personal details along with a chosen username and password
    Then their user account is created, and they are logged into the NutriPapi system

  Scenario: Attempt to Create an Account with an Existing Email (Error Flow)
    Given the visitor is on the NutriPapi account creation page
    When they attempt to create an account using an email address that is already associated with an existing account
    Then a "Email already in use" error message is displayed

  Scenario: Attempt to Create an Account without Mandatory Fields (Error Flow)
    Given the visitor is on the NutriPapi account creation page
    When they attempt to submit the account creation form without filling out all mandatory fields
    Then an "All fields are required" error message is displayed
