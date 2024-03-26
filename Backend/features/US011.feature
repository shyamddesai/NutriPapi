Feature: Account Deletion
  As a user who no longer wishes to use the NutriPapi system, 
  I want to be able to delete my account 
  so that my personal data is removed from the system.

  Scenario: Successful Account Deletion (Normal Flow)
    Given the user has logged into the NutriPapi system and navigates to the account settings page
    When the user has selected the option to delete their account and they confirm their decision by entering the correct password
    Then the system permanently deletes their account and all associated personal data, displaying a confirmation message that their account has been successfully deleted.

  Scenario: Attempt to Delete Account without Confirmation (Error Flow)
    Given the user has logged into the NutriPapi system and navigates to the account settings page
    When the user has selected the option to delete their account and they enter the incorrect password and fail to confirm the account deletion
    Then the system does not delete their account, displaying an error message such as "The password entered is incorrect. Please retry to proceed with account deletion."
