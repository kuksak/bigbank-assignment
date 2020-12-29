import unittest

import requests

from unit_tests.utility import json_request, CALCULATE_API_URL


class TestCalculatorModalProductType(unittest.TestCase):

    def test_calculate_monthly_installment_when_invalid_product_type(self):
        json_data = json_request(126, 30000, 10.95, 27, product_type='ZZZXX')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500)
