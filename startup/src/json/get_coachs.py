from lib.api import get_response
from lib.etc import append_json
from lib.postgres import PostgresConnector
import os

def append_coachs():
    
    conn = PostgresConnector(database='football')
    query = "SELECT team_id FROM teams"
    returned = conn.fetchall(query=query)
    
    endpoint = 'coachs'
    
    for index in returned:
        id = index[0]
        params = {"team": id}
        response = get_response(endpoint, params)
        dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/coachs/coachs_{id}.json"
        append_json(response, dir)
