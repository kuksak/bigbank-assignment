from behave import *
from selenium.webdriver.common.keys import Keys

from pages.calculator_modal import calculator_modal

use_step_matcher("re")


def clear_input_fields_and_assign_new_value(element, new_value):
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys(Keys.BACKSPACE)
    element.send_keys(new_value)
    calculator_modal.find_elements_by_class('bb-modal__body')[0].click()


@given("case 1: user edits the loan amount")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    calculator_modal.load_modal()


@when("user tries to enter alphabet for loan amount")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    clear_input_fields_and_assign_new_value(elements[0], 'a')


@then("case 1:loan amount field should not change")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    assert (elements[0].text != 'a')


@given("case 2: user edits the loan amount")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    calculator_modal.load_modal()


@when("user tries to enter negative loan amount value")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    clear_input_fields_and_assign_new_value(elements[0], '-10000')


@then("case 2: loan amount field should not change")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    assert (elements[0].text != '-10000 ')


@given("case 1: user edits the loan period")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    calculator_modal.load_modal()


@when("user tries to enter alphabet for loan period")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    clear_input_fields_and_assign_new_value(elements[1], 'a')


@then("case 1: loan period field should not change")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    assert (elements[1].text != 'a')


@given("case 2: user edits the loan period")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    calculator_modal.load_modal()


@when("user tries to enter negative value for loan period")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    clear_input_fields_and_assign_new_value(elements[1], '-124')


@then("case 2: loan period field should not change")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    assert (elements[1].text != '-124')


@given("case 3: user edits the loan amount")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    calculator_modal.load_modal()


@when("user tries to enter loan amount higher than maximum loan amount limit")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    clear_input_fields_and_assign_new_value(elements[0], '600000')


@then("case 3: loan amount field should change to default maximum loan amount")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    assert (elements[0].text != '600000')
    ## default highest value
    assert (elements[0].text == '500000')


@given("case 4: user edits the loan amount")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    calculator_modal.load_modal()


@when("user tries to enter loan amount lower than minimum loan amount limit")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    clear_input_fields_and_assign_new_value(elements[0], '9999')


@then("case 4: loan amount field should change to default minimum loan amount")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    assert (elements[0].text != '9999')
    ## default lowest value
    assert (elements[0].text == '10000')


@given("case 3: user edits the loan period")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    calculator_modal.load_modal()


@when("user tries to enter value higher than maximum loan period limit")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    clear_input_fields_and_assign_new_value(elements[1], '148')


@then("case 3: loan period field should change to default maximum loan period")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    assert (elements[1].text != '148')
    ## default highest value
    assert (elements[1].text == '144')


@given("case 4: user edits the loan period")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    calculator_modal.load_modal()


@when("user tries to enter value lower than minimum loan period limit")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    clear_input_fields_and_assign_new_value(elements[1], '9')


@then("case 4: loan period field should change to default minimum loan period")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    assert (elements[1].text != '9')
    ## default lowest value
    assert (elements[1].text == '12')


@given("case 5: user edits the loan amount")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    calculator_modal.load_modal()


@when("loan amount is in the valid range")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    clear_input_fields_and_assign_new_value(elements[0], '20000')


@then("case 5: estimated monthly cost should change and get reflected on the UI based on loan amount")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    assert (elements[0].text == '20000')
    assert (calculator_modal.find_elements_by_class('bb-calculator__result-value')[0].text is not None)


@given("case 5: user edits the loan period")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    calculator_modal.load_modal()


@when("loan period is in the valid range")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    clear_input_fields_and_assign_new_value(elements[1], '20')


@then("case 5: estimated monthly cost should change and get reflected on the UI based on loan period")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    elements = calculator_modal.find_elements_by_class('bb-slider__input')
    assert (elements[1].text == '20')
    assert (calculator_modal.find_elements_by_class('bb-calculator__result-value')[0].text is not None)
