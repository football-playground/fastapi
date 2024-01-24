from lib.postgres import PostgresConnector
import os
import json

def upload_venues():
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
                    venue_id = data["venue"]["id"]
                    venue_name = data["venue"]["name"]
                    venue_address = data["venue"]["address"]
                    venue_city = data["venue"]["city"]
                    venue_capacity = data["venue"]["capacity"]
                    venue_surface = data["venue"]["surface"]
                    venue_image = data["venue"]["image"]
                    
                    # set query
                    query = """INSERT INTO venues (team_id, venue_id, venue_name, venue_address, venue_city, venue_capacity, venue_surface, venue_image) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                    values = (team_id, venue_id, venue_name, venue_address, venue_city, venue_capacity, venue_surface, venue_image)
                    
                    # insert datas
                    try:
                        conn.commit(query=query, values=values)
                    except Exception as E:
                        print(E)

        conn.close()
    