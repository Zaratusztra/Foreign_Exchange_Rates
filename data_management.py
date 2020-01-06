import requests
import json

import logging

def get_latest_exchange_rates(base):
    """Placeholder"""
    logging.basicConfig(filename='data_management.log', level=logging.DEBUG)
    req = "https://api.exchangeratesapi.io/latest?base={}".format(base)
    response = requests.get(req)
    response = json.loads(response.text)
    return response