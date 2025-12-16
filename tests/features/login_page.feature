Feature: Loin Page Feature
    Scenario: Login -positive flow
        Given I am on the Login Page
        When I login with username 'standard_user' and password 'secret_sauce'
        Then I validate the page title
    