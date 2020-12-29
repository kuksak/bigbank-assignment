from behave import *

from pages.loan_page import loan_page

use_step_matcher("re")


@given("user is on Bigbank Sweden loan origination User Information form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("the page loads for the first time")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.find_element_by_id("personalDetailsForm")


@then("a fresh form without validation errors should load")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    element = loan_page.find_element_by_xpath('//form[@id="personalDetailsForm"]/div[@data-vv-as="Förnamn"]')
    assert (element.get_attribute('data-valid') is None)


@given("user submits the form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("no inputs are provided")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    submit_button = loan_page.find_element_by_id('personalDetailsForm-submit')
    submit_button.click()


@then("errors on the UI should appear for the user and form should not be submitted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    element = loan_page.find_element_by_xpath('//form[@id="personalDetailsForm"]/div[@data-vv-as="Förnamn"]')
    assert (element.get_attribute('data-valid') == "false")
    assert (loan_page.find_element_by_xpath('//div[@data-vv-as="Förnamn"]/p').text == 'Fältet Förnamn är obligatoriskt')

    element = loan_page.find_element_by_xpath('//form[@id="personalDetailsForm"]/div[@data-vv-as="Efternamn"]')
    assert (element.get_attribute('data-valid') == "false")
    assert (loan_page.find_element_by_xpath(
        '//div[@data-vv-as="Efternamn"]/p').text == 'Fältet Efternamn är obligatoriskt')

    element = loan_page.find_element_by_xpath('//form[@id="personalDetailsForm"]/div[@data-vv-as="Personnummer"]')
    assert (element.get_attribute('data-valid') == "false")
    assert (loan_page.find_element_by_xpath(
        '//div[@data-vv-as="Personnummer"]/p').text == 'Fältet Personnummer är obligatoriskt')

    element = loan_page.find_element_by_xpath('//form[@id="personalDetailsForm"]/div[@data-vv-as="E-postadress"]')
    assert (element.get_attribute('data-valid') == "false")
    assert (loan_page.find_element_by_xpath(
        '//div[@data-vv-as="E-postadress"]/p').text == 'Fältet E-postadress är obligatoriskt')

    element = loan_page.find_element_by_xpath('//form[@id="personalDetailsForm"]/div[@data-vv-as="Mobilnummer"]')
    assert (element.get_attribute('data-valid') == "false")
    assert (loan_page.find_element_by_xpath('//div[@data-vv-as="Mobilnummer"]/p').text == 'Mobilnummer Obligatoriskt')

    element = loan_page.find_element_by_xpath('//form[@id="personalDetailsForm"]/div[@data-vv-as="Lånesyfte"]')
    assert (element.get_attribute('data-valid') == "false")
    assert (loan_page.find_element_by_xpath(
        '//div[@data-vv-as="Lånesyfte"]/p').text == 'Fältet Lånesyfte är obligatoriskt')


@given("user enters identification number on the form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("identification number is invalid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    personal_identity_code = loan_page.find_element_by_id('personalIdentityCodeField')
    personal_identity_code.send_keys('abcdefghhhhhh')
    loan_page.find_element_by_xpath("//body").click()


@then(
    "validation error with error message “Personnummer måste passa ihop ÅÅMMDD-XXXX\.Sökande måste vara minst 20 år\.” should appear")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    personal_identity_code_element = loan_page.find_element_by_xpath('//div[@data-vv-as="Personnummer"]/p')
    assert (
            personal_identity_code_element.text == 'Personnummer måste passa ihop ÅÅMMDD-XXXX. Sökande måste vara minst 20 år.')


@given("user enters e-mail address")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("email address is not in the expected format")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    email_element = loan_page.find_element_by_id('emailField')
    email_element.send_keys('afdalfjfalfjdla.')
    loan_page.find_element_by_xpath("//body").click()


@then(
    "validation error with error message “Fältet E-postadress måste vara en giltig e-postadress”   should appear and form should not be submitted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    email_element = loan_page.find_element_by_xpath('//div[@data-vv-as="E-postadress"]/p')
    assert (email_element.text == 'Fältet E-postadress måste vara en giltig e-postadress')


@given("user enters mobile number")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("mobile number is invalid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    mobile_number_element = loan_page.find_element_by_name('phone')
    mobile_number_element.send_keys('7899889')
    loan_page.find_element_by_xpath("//body").click()


@then("validation error with error message should appear and form should not be submitted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    mobile_number_element = loan_page.find_element_by_xpath('//div[@data-vv-as="Mobilnummer"]/p')
    assert (mobile_number_element.text == 'Mobilnummer Obligatoriskt')


@given("user selects borrowing purpose")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("none of the option is selected")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    borrowing_purpose_element = loan_page.find_element_by_id('loanPurposeField')
    borrowing_purpose_element.click()
    loan_page.find_element_by_xpath("//body").click()


@then(
    'validation error with error message "Fältet Lånesyfte är obligatoriskt" should appear and form should not be submitted')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    borrowing_purpose_element = loan_page.find_element_by_xpath('//div[@data-vv-as="Lånesyfte"]/p')
    assert (borrowing_purpose_element.text == "Fältet Lånesyfte är obligatoriskt")


@given("user enters first name in the loan form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("first name is not empty")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    first_name_element = loan_page.find_element_by_id('firstNameField')
    first_name_element.send_keys("Jane")
    loan_page.find_element_by_xpath("//body").click()


@then("no error message should be displayed for first name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    first_name_value = loan_page.find_element_by_xpath('//div[@data-vv-as="Förnamn"]')
    assert (first_name_value.get_attribute('data-valid') == 'true')


@given("user enters Last name in the loan form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("Last name is not empty")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    last_name_element = loan_page.find_element_by_id('surnameField')
    last_name_element.send_keys("Doe")
    loan_page.find_element_by_xpath("//body").click()


@then("no error message should be displayed for last name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    last_name_element = loan_page.find_element_by_xpath('//div[@data-vv-as="Efternamn"]')
    assert (last_name_element.get_attribute('data-valid') == 'true')


@given("user enters Personal number in the loan form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("user input is in valid YYMMDD-XXXX format")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    personal_identity_code_element = loan_page.find_element_by_id('personalIdentityCodeField')
    personal_identity_code_element.send_keys("610321-3499")
    loan_page.find_element_by_xpath("//body").click()


@then("no error message should be displayed for Personal number")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    personal_identity_code_element = loan_page.find_element_by_xpath('//div[@data-vv-as="Personnummer"]')
    assert (personal_identity_code_element.get_attribute('data-valid') == 'true')


@given("user enters Email address in the loan form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("user email id is in correct format")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    email_element = loan_page.find_element_by_id('emailField')
    email_element.send_keys("janedoe@gmail.com")
    loan_page.find_element_by_xpath("//body").click()


@then("no error message should be displayed for email address")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    email_element = loan_page.find_element_by_xpath('//div[@data-vv-as="E-postadress"]')
    assert (email_element.get_attribute('data-valid') == 'true')


@given("user enters Mobile Number in the loan form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("mobile number is valid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    mobile_number_element = loan_page.find_element_by_name('phone')
    mobile_number_element.send_keys("766920539")
    loan_page.find_element_by_xpath("//body").click()


@then("no error message should be displayed for Mobile number")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    mobile_number_element = loan_page.find_element_by_xpath('//div[@data-vv-as="Mobilnummer"]')
    assert (mobile_number_element.get_attribute('data-valid') == 'true')


@given("user selects borrowing purpose drop down")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("a non-empty valid borrowing purpose")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    borrowing_purpose_element = loan_page.find_element_by_id('loanPurposeField')
    borrowing_purpose_element.send_keys("Konsumtion")
    loan_page.find_element_by_xpath("//body").click()


@then("no error message should be displayed borrowing purpose")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    borrowing_purpose_element = loan_page.find_element_by_xpath('//div[@data-vv-as="Lånesyfte"]')
    assert (borrowing_purpose_element.get_attribute('data-valid') == 'true')


@given("user enters email address")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("email address is incorrect")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    email_element = loan_page.find_element_by_id('emailField')
    email_element.send_keys("janedoe@")


@then("“CONTINUE” button is disabled and GREYED")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    submit_button = loan_page.find_element_by_id('personalDetailsForm-submit')
    assert ('bb-button--disabled' in submit_button.get_attribute('class'))


@given("user enters all fields")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.load_page()


@when("all the entered fields are correct")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    loan_page.find_element_by_id('firstNameField').send_keys("Jane")
    loan_page.find_element_by_id('surnameField').send_keys("Doe")
    loan_page.find_element_by_id('personalIdentityCodeField').send_keys("610321-3499")
    loan_page.find_element_by_id('emailField').send_keys("janedoe@gmail.com")
    loan_page.find_element_by_name('phone').send_keys("766920539")
    loan_page.find_element_by_id('loanPurposeField').send_keys("Konsumtion")


@then("“CONTINUE” button is enabled and GREEN")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    submit_button = loan_page.find_element_by_id('personalDetailsForm-submit')
    assert ('bb-button--green' in submit_button.get_attribute('class'))
