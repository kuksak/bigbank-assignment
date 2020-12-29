Feature: UI form fields validation

  Scenario: Validation errors in BigBank Sweden loan origination User Information form

    Given user is on Bigbank Sweden loan origination User Information form
    When the page loads for the first time
    Then a fresh form without validation errors should load

    Given user submits the form
    When no inputs are provided
    Then errors on the UI should appear for the user and form should not be submitted

    Given user enters identification number on the form
    When identification number is invalid
    Then validation error with error message “Personnummer måste passa ihop ÅÅMMDD-XXXX.Sökande måste vara minst 20 år.” should appear

    Given user enters e-mail address
    When email address is not in the expected format
    Then validation error with error message “Fältet E-postadress måste vara en giltig e-postadress”   should appear and form should not be submitted

    Given user enters mobile number
    When mobile number is invalid
    Then validation error with error message should appear and form should not be submitted

    Given user selects borrowing purpose
    When none of the option is selected
    Then validation error with error message "Fältet Lånesyfte är obligatoriskt" should appear and form should not be submitted


  Scenario: Successful field validations in BigBank Sweden loan origination User Information form

    Given user enters first name in the loan form
    When first name is not empty
    Then no error message should be displayed for first name

    Given user enters Last name in the loan form
    When Last name is not empty
    Then no error message should be displayed for last name

    Given user enters Personal number in the loan form
    When user input is in valid YYMMDD-XXXX format
    Then no error message should be displayed for Personal number

    Given user enters Email address in the loan form
    When user email id is in correct format
    Then no error message should be displayed for email address

    Given user enters Mobile Number in the loan form
    When mobile number is valid
    Then no error message should be displayed for Mobile number

    Given user selects borrowing purpose drop down
    When a non-empty valid borrowing purpose
    Then no error message should be displayed borrowing purpose

  Scenario: Form submission disabled if any field is incorrect or missing

    Given user enters email address
    When email address is incorrect
    Then “CONTINUE” button is disabled and GREYED

    Given user enters all fields
    When all the entered fields are correct
    Then “CONTINUE” button is enabled and GREEN










