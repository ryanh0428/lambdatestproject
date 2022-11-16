Feature: sauce website login function

    Scenario: A standard user try to login
        Given user is on the sauce demo webpage
        When the user type in the user name "standard_user" and password "secret_sauce"
        Then the user is directed to inventory page "https://www.saucedemo.com/inventory.html"