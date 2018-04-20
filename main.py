import json
import datetime
from xero import Xero
from xero.auth import PrivateCredentials


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

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
    
    # Convert datetime to str to make the data serializable
    str_response = json.dumps(response, default=myconverter)
    return json.loads(str_response)