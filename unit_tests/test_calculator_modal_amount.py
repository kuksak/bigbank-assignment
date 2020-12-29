import unittest

import requests

from unit_tests.utility import json_request, CALCULATE_API_URL


class TestCalculatorModalAmount(unittest.TestCase):

    def test_calculate_monthly_installment_when_all_valid_input_fields(self):
        json_data = json_request(126, 30000, 10.95, 27)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 56003.02, 444.47, 14.87)

    # Test for total loan amount
    def test_calculate_monthly_installment_when_negative_amount_then_response_200(self):
        json_data = json_request(126, -500000, 10.95, 27)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        # FIXME: API returns 200 response even though input is invalid
        self.perform_assertions(json_response, -494960, 40, 0)

    def test_calculate_monthly_installment_when_maximum_loan_then_response_200(self):
        json_data = json_request(144, 500000, 10.95, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 909973.41, 6319.27, 11.87)

    def test_calculate_monthly_installment_when_loan_amount_greater_than_maximum_then_default_maximum_amount(self):
        json_data = json_request(100, 600000, 10.95, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 923509.98, 9235.11, 11.86)

    def test_calculate_monthly_installment_when_minimum_loan_then_response_200(self):
        json_data = json_request(12, 10000, 10.95, 14)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 11053.79, 921.15, 41.61)

    def test_calculate_monthly_installment_when_loan_amount_less_than_minimum_then_default_minimum_amount(self):
        json_data = json_request(11, 900, 10.95, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 1387.6, 126.15, 41640.7)

    # testing if the admininstrative fee is negative
    def test_calculate_monthly_installment_when_negative_administrative_fee(self):
        json_data = json_request(126, 30000, 10.95, 27, -30000)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, -3729036.98, -29595.53, 47605234.05)

    def perform_assertions(self, json_response, expected_repayable_amount, expected_monthy_amount, expected_apr):
        self.assertEqual(json_response['totalRepayableAmount'], expected_repayable_amount)
        self.assertEqual(json_response['monthlyPayment'], expected_monthy_amount)
        self.assertEqual(json_response['apr'], expected_apr)
