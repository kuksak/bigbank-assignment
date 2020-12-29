import unittest

import requests

from unit_tests.utility import json_request, CALCULATE_API_URL


class TestCalculatorModalCurrency(unittest.TestCase):
    pass

    def test_calculate_monthly_installment_when_invalid_currency_then_response_500(self):
        json_data = json_request(126, 30000, 10.95, 27, currency='Blah')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.status_code == 500)

    def test_calculate_monthly_installment_when_invalid_currency_with_three_characters(self):
        json_data = json_request(126, 30000, 10.95, 27, currency='ZZZ')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        ## FIXME: we are accepting any three digits, which is not a valid currency and the response is 200 expected ?
        self.assertFalse(response.status_code == 500)

    def test_calculate_monthly_installment_when_currency_euros(self):
        json_data = json_request(126, 30000, 10.95, 27, currency='EUR')
        response = requests.post(CALCULATE_API_URL, json=json_data)
        self.assertTrue(response.ok)
