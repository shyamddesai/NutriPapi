Feature: Secure Authentication and Data Encryption
  As a NutriPapi user concerned about my personal data,
  I want the NutriPapi system to implement secure authentication methods and encrypt sensitive user data
  to ensure my privacy and security.

  Scenario: Implementing Secure Authentication (Normal Flow)
    Given a new or returning user is accessing the NutriPapi system,
    When they attempt to log in or register,
    Then the system requires a secure authentication method, such as bcrypt, in addition to the standard username and password, to verify the user's identity and protect against unauthorized access.

  Scenario: Encrypting Sensitive User Data (Normal Flow)
    Given a user inputs or updates their personal health information in the NutriPapi system (such as weight, dietary preferences, or health goals),
    When this data is stored or transmitted by the NutriPapi system,
    Then all sensitive user data is encrypted using industry-standard encryption protocols to ensure that it remains confidential and secure against data breaches and unauthorized access.

  Scenario: Unauthorized Access Attempt Detected (Error Flow)
    Given an attempt is made to access a user's account with incorrect login details multiple times,
    When the system detects these repeated unauthorized access attempts,
    Then it temporarily locks the account and sends an alert to the user's email or phone, advising them of the suspicious activity and providing steps to secure their account, such as resetting their password or enabling two-factor authentication.
