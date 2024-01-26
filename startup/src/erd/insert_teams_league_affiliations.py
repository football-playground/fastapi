from lib.postgres import PostgresConnector
import os
import json

def upload_teams_league_affiliations():
    # create conn
    conn = PostgresConnector(database="football")
    
    directory_path = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/teams"
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                
                league_id = data["parameters"]["league"]
                season = data["parameters"]["season"]

                for data in data["response"]:
                    # params
                    team_id = data["team"]["id"]
                                        
                    # set query
                    query = """INSERT INTO teams_league_affiliations (season, team_id, league_id) 
                    VALUES (%s, %s, %s)"""
                    values = (season, team_id, league_id)
                    
                    # insert datas
                    try:
                        conn.commit(query=query, values=values)
                    except Exception as E:
                        print(E)

    conn.close()
    