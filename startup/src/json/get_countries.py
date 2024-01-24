from lib.api import get_response
from lib.etc import append_json
import os

def append_countries():
    endpoint = 'countries'
    response = get_response(endpoint)
    dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/countries/countries.json"
    append_json(response, dir)
