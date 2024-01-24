from lib.postgres import PostgresConnector
import os
import json

def upload_player_sidelined():
    # create conn
    conn = PostgresConnector(database="football")
    
    directory_path = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/sidelined/players"
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                
                coach_id = data["parameters"]["player"]

                for sideline in data["response"]:
                    # params
                    player_sidelined_type = sideline["type"]
                    player_sidelined_start = sideline["start"]
                    player_sidelined_end = sideline["end"]
                                        
                    # set query
                    query = """INSERT INTO player_sidelined 
                    (coach_id, player_sidelined_type, player_sidelined_start, player_sidelined_end) 
                    VALUES (%s, %s, %s, %s)"""
                    values = (coach_id, player_sidelined_type, player_sidelined_start, player_sidelined_end)
                    
                    # insert datas
                    try:
                        conn.commit(query=query, values=values)
                    except Exception as E:
                        print(E)

        conn.close()