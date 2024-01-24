from lib.postgres import PostgresConnector
import os
import json

def upload_leagues():
    # create conn
    conn = PostgresConnector(database="football")
    
    # read json
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/leagues/leagues.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    for data in data["response"]:
        # params
        league_id = data["league"]["id"]
        league_name = data["league"]["name"]
        league_logo = data["league"]["logo"]
        country_name = data["country"]["name"]
        
        # set query
        query = "INSERT INTO leagues (league_id, league_name, league_logo, country_name) VALUES (%s, %s, %s, %s)"
        values = (league_id, league_name, league_logo, country_name)
        
        # insert datas
        try:
            conn.commit(query=query, values=values)
        except Exception as E:
            print(E)

    conn.close()
    