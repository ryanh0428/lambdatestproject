Feature: sauce website login function

    Scenario: A standard user try to login
        Given user is on the sauce demo webpage
        When the user type in the user name "standard_user" and password "secret_sauce"
        Then the user is directed to inventory page "https://www.saucedemo.com/inventory.html"

        When the user click the filter menu on the right hand side
        Then 4 options is avilable to user: "Name (A to Z)","Name (Z to A)","Price (low to high)","Price (high to low)"