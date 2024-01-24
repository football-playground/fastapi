from lib.api import get_response
from lib.etc import append_json
import os

def append_leagues():
    endpoint = 'leagues'
    params = {'type': 'League'}
    response = get_response(endpoint, params)
    dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/leagues/leagues.json"
    append_json(response, dir)
