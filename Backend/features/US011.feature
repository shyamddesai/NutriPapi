Feature: Account Deletion
  As a user who no longer wishes to use the NutriPapi system, 
  I want to be able to delete my account 
  so that my personal data is removed from the system.

  Scenario: Successful Account Deletion (Normal Flow)
    Given the user has logged into the NutriPapi system and navigated to the profile page,
    When they select the option to delete their account and confirm their decision by entering their password,
    Then the system permanently deletes their account and all associated personal data, displaying a confirmation message that their account has been successfully deleted.

  Scenario: Attempt to Delete Account without Confirmation (Error Flow)
    Given the user has selected the option to delete their account in the NutriPapi system,
    When they fail to confirm the account deletion by not entering their password correctly,
    Then the system does not delete their account, displaying an error message such as "Account deletion not confirmed. Please confirm to proceed with account deletion."
