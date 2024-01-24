from lib.api import get_response
from lib.etc import append_json
from lib.postgres import PostgresConnector
import os

def append_players():
    conn = PostgresConnector(database='football')
    query = "SELECT team_id FROM teams"
    returned = conn.fetchall(query=query)
    
    endpoint = 'players'
    
    for index in returned:
        id = index[0]
        for page in range (1, 11):
            params = {"team": id, "season": 2023, "page":page}
            response = get_response(endpoint, params)
            dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/players/players_{id}_{page}.json"
            append_json(response, dir)
