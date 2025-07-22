Feature: Manage a single to-do item

  Scenario: User adds, completes, and deletes a to-do item
    Given the user is logged in
    When the user adds a to-do item "shop"
    And marks the item "shop" as completed
    And deletes the item "shop"
    Then the item "shop" should no longer appear in the list
