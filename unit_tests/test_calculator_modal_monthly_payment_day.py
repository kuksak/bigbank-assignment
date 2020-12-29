import unittest

import requests

from unit_tests.utility import json_request, CALCULATE_API_URL


class TestCalculatorModalMonthlyPaymentDay(unittest.TestCase):

    def test_calculate_monthly_installment_when_valid_monthly_payment_day(self):
        json_data = json_request(126, 500000, 10.95, 1)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 855586.33, 6790.37, 11.87)

    def test_calculate_monthly_installment_when_invalid_monthly_payment_day(self):
        ## FIXME: do we expect monthly payment days to be in the range 1-31?
        monthly_payment_day = 32
        json_data = json_request(126, 500000, 10.95, monthly_payment_day)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 855335.77, 6788.38, 11.87)

    def perform_assertions(self, json_response, expected_repayable_amount, expected_monthy_amount, expected_apr):
        self.assertEqual(json_response['totalRepayableAmount'], expected_repayable_amount)
        self.assertEqual(json_response['monthlyPayment'], expected_monthy_amount)
        self.assertEqual(json_response['apr'], expected_apr)
