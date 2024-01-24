from lib.postgres import PostgresConnector
import os
import json

def upload_players():
    # create conn
    conn = PostgresConnector(database="football")
    
    directory_path = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/players"
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

                for player in data["response"]:
                    # params
                    player_id = player["player"]["id"]
                    player_firstname = player["player"]["firstname"]
                    player_lastname = player["player"]["lastname"]
                    player_birth = player["player"]["birth"]["date"]
                    player_place = player["player"]["birth"]["place"]
                    player_country = data["player"]["birth"]["country"]
                    player_nationality = player["player"]["nationality"]
                    player_height = player["player"]["height"].split(" cm")[0] if player["player"]["height"] != None else None
                    player_weight = player["player"]["weight"].split(" kg")[0] if player["player"]["weight"] != None else None
                    player_photo = player["player"]["photo"]
                    
                    # set query
                    query = """INSERT INTO players 
                    (player_id, player_firstname, player_lastname, player_birth, player_place, player_country, player_nationality, player_height, player_weight, player_photo) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    values = (player_id, player_firstname, player_lastname, player_birth, player_place, player_country, player_nationality, player_height, player_weight, player_photo)
                    
                    # insert datas
                    try:
                        conn.commit(query=query, values=values)
                    except Exception as E:
                        print(E)

        conn.close()
    