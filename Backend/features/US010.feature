Feature: Diverse Recipe Recommendations in the NutriPapi System
  As a user who enjoys culinary diversity,
  I want the NutriPapi system to recommend a variety of recipes for different meals each day
  and ensure that the same meal is not repeated within a two-week period unless I specifically request it.

  Scenario: Successfully recommending diverse recipes (Normal Flow)
    Given the user accesses the meal recommendation feature on the NutriPapi system.
    When the system generates meal recommendations for the day.
    Then it should recommend a variety of recipes for different meals that have not been recommended to the user in the past two weeks.

  Scenario: User with many dietary restrictions challenges the system (Alternate Flow)
    Given the user has multiple dietary restrictions set in the NutriPapi system.
    When the system generates meal recommendations for the day.
    Then it should make an effort to provide diverse recipes considering the dietary restrictions, but if the restrictions limit available options, it may result in repeated recipes within the two-week period.

  Scenario: Preventing repeated recipes without specific request (Error Flow)
    Given the system has recommended a specific recipe to the user within the last two weeks.
    When the system generates new meal recommendations for the day.
    Then it should not include any recipes that have been recommended within the past two weeks unless the user has specifically requested a repeat of those recipes.