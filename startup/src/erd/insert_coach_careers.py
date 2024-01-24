from lib.postgres import PostgresConnector
import os
import json

# Need to fix or not

def upload_coach_careers():
    # create conn
    conn = PostgresConnector(database="football")
    
    directory_path = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/coachs"
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

                for coach in data["response"]:
                    # params
                    coach_id = coach["id"]
                    season = 2023
                    team_id = coach["career"][0]["team"]["id"]
                    coach_start = coach["career"][0]["start"]
                    coach_end = coach["career"][0]["end"]
                
                    # set query
                    query = """INSERT INTO coach_careers
                    (coach_id, season, team_id, coach_start, coach_end) 
                    VALUES (%s, %s, %s, %s, %s)"""
                    values = (coach_id, season, team_id, coach_start, coach_end)
                    
                    # insert datas
                    try:
                        conn.commit(query=query, values=values)
                    except Exception as E:
                        print(E)

        conn.close()
    