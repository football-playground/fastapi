from lib.api import get_response
from lib.etc import append_json
from lib.postgres import PostgresConnector
import os

def append_transfers():
    
    conn = PostgresConnector(database='football')
    query = "SELECT player_id FROM players"
    returned = conn.fetchall(query=query)
    
    endpoint = 'transfers'
    
    for index in returned:
        id = index[0]
        params = {"player": id}
        response = get_response(endpoint, params)
        dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/transfers/transfers_{id}.json"
        append_json(response, dir)
