import os
import json
from configparser import ConfigParser

def get_config_values(sets:list):
    # create config
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../config/config.ini")
    config = ConfigParser()
    config.read(config_path)
    
    # read values
    returned = [config.get(category, key) for (category, key) in sets]
    
    return returned

def append_json(data:dict, dir:str):
    with open(dir, "a", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
if __name__ == "__main__":
    sets = [("postgres", "host"), ("postgres", "port"), ("postgres", "user"), ("postgres", "password")]
    returend = get_config_values(sets)
    print(returend)
    
    data = {"value": "Hello, World1!", "datetime": "unknown"}
    dir = "/Users/kimdohoon/git/football-playground/fastapi/startup/datas/demo/demo.json"
    append_json(data, dir)