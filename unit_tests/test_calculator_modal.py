import unittest

from unit_tests.test_calculator_modal_amount import TestCalculatorModalAmount
from unit_tests.test_calculator_modal_currency import TestCalculatorModalCurrency
from unit_tests.test_calculator_modal_interest_rate import TestCalculatorModalInterestRate
from unit_tests.test_calculator_modal_maturity import TestCalculatorModalMaturity
from unit_tests.test_calculator_modal_monthly_payment_day import TestCalculatorModalMonthlyPaymentDay
from unit_tests.test_calculator_modal_product_type import TestCalculatorModalProductType


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestCalculatorModalMaturity))
    test_suite.addTest(unittest.makeSuite(TestCalculatorModalInterestRate))
    test_suite.addTest(unittest.makeSuite(TestCalculatorModalMonthlyPaymentDay))
    test_suite.addTest(unittest.makeSuite(TestCalculatorModalAmount))
    test_suite.addTest(unittest.makeSuite(TestCalculatorModalProductType))
    test_suite.addTest(unittest.makeSuite(TestCalculatorModalCurrency))
    return test_suite


if __name__ == '__main__':
    unittest.main()
