Feature: Open web browser
  Scenario: Visit Google
    Given I have a web browser
    When I navigate to "https://www.google.com"
    Then I can see the Google search page
