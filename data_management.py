import requests
import json

def get_latest_exchange_rates():
    """Placeholder"""
    response = requests.get("https://api.exchangeratesapi.io/latest")
    return response