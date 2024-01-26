from lib.postgres import PostgresConnector
import os
import json

def upload_countries():
    # create conn
    conn = PostgresConnector(database="football")
    
    # read json
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/countries/countries.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    for data in data["response"]:
        # params
        name = data["name"]
        code = data["code"]
        flag = data["flag"]
        
        # set query
        query = "INSERT INTO countries VALUES (%s, %s, %s)"
        values = (name, code, flag)
        
        # insert datas
        try:
            conn.commit(query=query, values=values)
        except Exception as E:
            raise ValueError(E)
    
    conn.close()
            