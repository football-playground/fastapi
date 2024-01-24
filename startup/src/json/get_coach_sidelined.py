from lib.api import get_response
from lib.etc import append_json
from lib.postgres import PostgresConnector
import os

def append_coach_sidelined():
    
    conn = PostgresConnector(database='football')
    query = "SELECT coach_id FROM coachs"
    returned = conn.fetchall(query=query)
    
    endpoint = 'sidelined'
    
    for index in returned:
        id = index[0]
        params = {"coach": id}
        response = get_response(endpoint, params)
        dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/sidelined/coachs/coach_sidelined_{id}.json"
        append_json(response, dir)
