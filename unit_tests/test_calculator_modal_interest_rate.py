import unittest

import requests

from unit_tests.utility import json_request, CALCULATE_API_URL


class TestCalculatorModalInterestRate(unittest.TestCase):

    def test_calculate_monthly_installment_when_constant_interest_rate(self):
        json_data = json_request(126, 500000, 10.95, 1)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 855586.33, 6790.37, 11.87)

    def test_calculate_monthly_installment_when_negative_interest_rate(self):
        ## FIXME: negative interest rate causes APR to be zero but the total repayable and monthly amount are still calculated
        json_data = json_request(126, 500000, -10.95, 27)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 505040, 4008.26, 0)

    def perform_assertions(self, json_response, expected_repayable_amount, expected_monthy_amount, expected_apr):
        self.assertEqual(json_response['totalRepayableAmount'], expected_repayable_amount)
        self.assertEqual(json_response['monthlyPayment'], expected_monthy_amount)
        self.assertEqual(json_response['apr'], expected_apr)
