from lib.postgres import PostgresConnector
import os
import json

def upload_coach_sidelined():
    # create conn
    conn = PostgresConnector(database="football")
    
    directory_path = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/sidelined/coachs"
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith('.json'):
            
            try:
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    
                    coach_id = data["parameters"]["coach"]

                    for sideline in data["response"]:
                        # params
                        coach_sidelined_type = sideline["type"]
                        coach_sidelined_start = sideline["start"]
                        coach_sidelined_end = sideline["end"]
                                            
                        # set query
                        query = """INSERT INTO coach_sidelined 
                        (coach_id, coach_sidelined_type, coach_sidelined_start, coach_sidelined_end) 
                        VALUES (%s, %s, %s, %s)"""
                        values = (coach_id, coach_sidelined_type, coach_sidelined_start, coach_sidelined_end)
                        
                        # insert datas
                        try:
                            conn.commit(query=query, values=values)
                        except Exception as E:
                            raise ValueError(E)
            except:
                print(filename)
                
    conn.close()