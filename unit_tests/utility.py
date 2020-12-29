CALCULATE_API_URL = 'https://ansokan.bigbank.se/api/v1/loan/calculate'


def json_request(maturity, amount, interest_rate, monthly_payment_day, administrative_fee=40, conclusion_fee=695,
                 currency='SEK', product_type='LOANSE02', ):
    return {
        "maturity": maturity,
        "productType": product_type,
        "amount": amount,
        "interestRate": interest_rate,
        "monthlyPaymentDay": monthly_payment_day,
        "administrationFee": administrative_fee,
        "conclusionFee": conclusion_fee,
        "currency": currency
    }
