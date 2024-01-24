from lib.postgres import PostgresConnector
import os
import json

def upload_league_seasons():
    # create conn
    conn = PostgresConnector(database="football")
    
    # read json
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/leagues/leagues.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    for league in data["response"]:
        # params
        league_id = league["league"]["id"]
        
        for season in league["seasons"]:
            year = season["year"]
            start = season["start"]
            end = season["end"]

            # set query
            query = "INSERT INTO league_seasons (league_id, season, start_date, end_date) VALUES (%s, %s, %s, %s)"
            values = (league_id, year, start, end)
            
            # insert datas
            try:
                conn.commit(query=query, values=values)
            except Exception as E:
                print(E)

    conn.close()
    