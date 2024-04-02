Feature: Secure Authentication and Data Encryption
  As a NutriPapi user concerned about my personal data,
  I want the NutriPapi system to implement secure authentication methods and encrypt sensitive user data
  to ensure my privacy and security.

  Scenario: Implementing Secure Authentication (Normal Flow)
    Given an user navigates to the registration page of the NutriPapi system
    When they attempt to register with valid credentials
    Then the system employs encrypted passwords for secure authentication to safeguard against unauthorized access

  Scenario: Encrypting Sensitive User Data (Normal Flow)
    Given a user inputs or updates their personal health information in the NutriPapi system
    When this data is stored or transmitted by the NutriPapi system
    Then all sensitive user data is encrypted using industry-standard encryption protocols to ensure that it remains confidential and secure against unauthorized access

  Scenario: Unauthorized Access Attempt Detected (Error Flow)
    Given repeated failed login attempts on a user's account
    When the system detects these unauthorized access attempts
    Then it temporarily locks the account to prevent further unauthorized access.
