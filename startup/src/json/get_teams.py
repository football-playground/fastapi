from lib.api import get_response
from lib.etc import append_json
import os

def append_teams():
    endpoint = 'teams'
    league_ids = [39, 40, 61, 62, 78, 79, 135, 136, 140, 141]
    
    for id in league_ids:
        params = {"league": id, "season": 2023}
        response = get_response(endpoint, params)
        dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/teams/teams_{id}.json"
        append_json(response, dir)
