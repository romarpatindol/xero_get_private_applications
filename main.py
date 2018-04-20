import json
import datetime
from xero import Xero
from xero.auth import PrivateCredentials


def main(consumer_key, rsa_key, query):
    try:
        credentials = PrivateCredentials(consumer_key, rsa_key)
        xero = Xero(credentials)
        xero_data = eval("xero." + query)

        response = {
            "data": xero_data
        }
    
    except Exception as e:
        response = {
            "error": e
        }
        
    return response