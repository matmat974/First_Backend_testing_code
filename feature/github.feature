# Created by matthew at 2/6/22
Feature: GitHub API validation
  # Enter feature description here

  Scenario: Session management check
    Given I have github auth credentials
    When I hit getRepo API of github
    Then status code of response should be 200
