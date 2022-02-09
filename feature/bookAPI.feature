# Created by matthew at 2/3/22

@addbook
Feature: Verify if books are added and deleted using Library API
  # Enter feature description here

  @library
  Scenario: Verify addbook API functionality
    Given the book which needs to be added to library
    When we execute the AddBook PostAPI method
    Then book is succesfully added
    And status code of response should be 200

  @library
  Scenario Outline: Verify addbook API functionality
    Given the book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is succesfully added
      Examples:
        | isbn |aisle |
        | bookID |00010 |
        | bookID |00011 |