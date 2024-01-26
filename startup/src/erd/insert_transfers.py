from lib.postgres import PostgresConnector
import os
import json

# Need to create season data

def upload_transfers():
    # create conn
    conn = PostgresConnector(database="football")
    
    directory_path = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/transfers"
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith('.json'):
            
            try:
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)

                    for player in data["response"]:
                        # params
                        player_id = player["player"]["id"]

                        for transfer in player["transfers"]:
                            transfer_date = transfer["date"]
                            team_id = transfer["teams"]["in"]["id"]
                    
                        # set query
                        query = """INSERT INTO transfers
                        (player_id, team_id, transfer_date) 
                        VALUES (%s, %s, %s)"""
                        values = (player_id, team_id, transfer_date)
                        
                        # insert datas
                        try:
                            conn.commit(query=query, values=values)
                        except Exception as E:
                            raise ValueError(E)
            except:
                print(filename)

    conn.close()
    