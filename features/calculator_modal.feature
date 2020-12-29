Feature: Calculator Modal fields validations and calculations of monthly payments

  Scenario: Input fields do not accept other characters than digits

    Given case 1: user edits the loan amount
    When user tries to enter alphabet for loan amount
    Then case 1:loan amount field should not change

    Given case 2: user edits the loan amount
    When user tries to enter negative loan amount value
    Then case 2: loan amount field should not change

    Given case 1: user edits the loan period
    When user tries to enter alphabet for loan period
    Then case 1: loan period field should not change

    Given case 2: user edits the loan period
    When user tries to enter negative value for loan period
    Then case 2: loan period field should not change

  Scenario: Loan amount and period default to maximum value if input is higher than maximum allowed limit

    Given case 3: user edits the loan amount
    When user tries to enter loan amount higher than maximum loan amount limit
    Then case 3: loan amount field should change to default maximum loan amount

    Given case 4: user edits the loan amount
    When user tries to enter loan amount lower than minimum loan amount limit
    Then case 4: loan amount field should change to default minimum loan amount

    Given case 3: user edits the loan period
    When user tries to enter value higher than maximum loan period limit
    Then case 3: loan period field should change to default maximum loan period

    Given case 4: user edits the loan period
    When user tries to enter value lower than minimum loan period limit
    Then case 4: loan period field should change to default minimum loan period

  Scenario: Monthly Estimated Values change when loan amount and period are in the valid range

    Given case 5: user edits the loan amount
    When loan amount is in the valid range
    Then case 5: estimated monthly cost should change and get reflected on the UI based on loan amount

    Given case 5: user edits the loan period
    When loan period is in the valid range
    Then case 5: estimated monthly cost should change and get reflected on the UI based on loan period


