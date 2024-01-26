from lib.postgres import PostgresConnector
import os
import json

def upload_coachs():
    # create conn
    conn = PostgresConnector(database="football")
    
    directory_path = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/coachs"
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith('.json'):
            
            try:
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)

                    for coach in data["response"]:
                        # params
                        coach_id = coach["id"]
                        coach_firstname = coach["firstname"]
                        coach_lastname = coach["lastname"]
                        coach_birth = coach["birth"]["date"]
                        coach_place = coach["birth"]["place"]
                        coach_country = coach["birth"]["country"]
                        coach_nationality = coach["nationality"]
                        coach_height = coach["height"].split(" cm")[0] if coach["height"] != None else None
                        coach_weight = coach["weight"].split(" kg")[0] if coach["weight"] != None else None
                        coach_photo = coach["photo"]
                        
                        # set query
                        query = """INSERT INTO coachs 
                        (coach_id, coach_firstname, coach_lastname, coach_birth, coach_place, coach_placecountry, coach_nationality, coach_height, coach_weight, coach_photo) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                        values = (coach_id, coach_firstname, coach_lastname, coach_birth, coach_place, coach_country, coach_nationality, coach_height, coach_weight, coach_photo)
                        
                        # insert datas
                        try:
                            conn.commit(query=query, values=values)
                        except Exception as E:
                            raise ValueError(E)
            except:
                print(filename)
                
    conn.close()
    