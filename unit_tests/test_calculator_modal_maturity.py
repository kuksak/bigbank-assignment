import unittest

import requests

from unit_tests.utility import json_request, CALCULATE_API_URL


class TestCalculatorModalMaturity(unittest.TestCase):

    def test_calculate_monthly_installment_when_all_valid_input_fields(self):
        json_data = json_request(126, 500000, 10.95, 27)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 854425.74, 6781.16, 11.87)

    # Test for maturity period
    def test_calculate_monthly_installment_when_negative_maturity_then_response_200(self):
        json_data = json_request(-1, 500000, 10.95, 27)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        # FIXME: API returns 200 response even though input is invalid
        self.perform_assertions(json_response, 0, 0, 5)

    def test_calculate_monthly_installment_when_maximum_maturity_then_response_200(self):
        json_data = json_request(144, 200000, 10.95, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 367444.99, 2551.71, 12.14)

    def test_calculate_monthly_installment_when_maturity_greater_than_maximum_then_default_maximum_maturity(self):
        json_data = json_request(1000, 200000, 10.95, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 2090853.7, 2169.17, 12)

    def test_calculate_monthly_installment_when_minimum_maturity_then_response_200(self):
        json_data = json_request(12, 400000, 10.95, 14)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 423432.09, 35286.01, 12.33)

    def test_calculate_monthly_installment_when_maturity_less_than_minimum_then_default_minimum_maturity(self):
        json_data = json_request(11, 200000, 10.95, 15)
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
        json_response = response.json()
        self.perform_assertions(json_response, 211015.01, 19183.19, 13.04)

    def perform_assertions(self, json_response, expected_repayable_amount, expected_monthy_amount, expected_apr):
        self.assertEqual(json_response['totalRepayableAmount'], expected_repayable_amount)
        self.assertEqual(json_response['monthlyPayment'], expected_monthy_amount)
        self.assertEqual(json_response['apr'], expected_apr)
