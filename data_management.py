import os
import requests
import json

import logging

def setup_logger(sep):
    fname = os.path.abspath(__file__)
    fname = fname.split(sep)
    fname[-1] = 'data_management.log'
    fname = sep.join(fname)
    
    logging.basicConfig(filename=fname, level=logging.DEBUG)

def get_latest_exchange_rates(base):
    """Auxiliary function, for connecting to the api.exchangeratesapi.io API and retrieving data."""
    if os.name == 'posix':
        sep = '/'
        setup_logger(sep)
    elif os.name == 'nt':
        sep = '\\'
        setup_logger(sep)
    else:
        logging.basicConfig(filename='foreign_exchange_rates.log', level=logging.CRITICAL)
    
    
    
    req = "https://api.exchangeratesapi.io/latest?base={}".format(base)
    response = requests.get(req)
    response = json.loads(response.text)
    return response
