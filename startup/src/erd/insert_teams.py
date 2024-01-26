from lib.postgres import PostgresConnector
import os
import json

def upload_teams():
    # create conn
    conn = PostgresConnector(database="football")
    
    directory_path = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/teams"
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

                for data in data["response"]:
                    # params
                    team_id = data["team"]["id"]
                    team_name = data["team"]["name"]
                    team_code = data["team"]["code"]
                    country_name = data["team"]["country"]
                    team_founded = data["team"]["founded"]
                    team_logo = data["team"]["logo"]
                    
                    # set query
                    query = """INSERT INTO teams (team_id, team_name, team_code, country_name, team_founded, team_logo) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""
                    values = (team_id, team_name, team_code, country_name, team_founded, team_logo)
                    
                    # insert datas
                    try:
                        conn.commit(query=query, values=values)
                    except Exception as E:
                        print(E)

    conn.close()
    