import requests
from lib.etc import *

def get_response(endpoint:str):
    # set url
    url = f'https://v3.football.api-sports.io/{endpoint}'

    # set headers
    [api_key] = get_config_values([('api', 'key')])
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }

    # get response
    response = requests.get(url, headers=headers).json()
    
    return response

def fixtures(fixtures_ids:str, league:str, date:str):
    try:
        # Airflow에서 스트링으로 변환
        #fixtures_ids_str = "-".join(map(str, fixtures_ids))
        endpoint_str = f"fixtures?ids={fixtures_ids}"
        dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/{league}/fixtures/{date}.json"
        # 또는 dir = "hdfs경로"
        response = get_response(endpoint_str)
        append_json(response, dir)
        return {"status": "success", "message": f"Fixtures for {date} in league {league} successfully saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def injuries(fixtures_id:str, league:str, date:str):
    try:
        # Airflow에서 스트링으로 변환
        #fixtures_ids_str = "-".join(map(str, fixtures_ids))
        endpoint_str = f"injuries?fixture={fixtures_id}"
        dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/{league}/injuries/{date}.json"
        # 또는 dir = "hdfs경로"
        response = get_response(endpoint_str)
        append_json(response, dir)
        return {"status": "success", "message": f"Injuries for {date} in league {league} successfully saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    endpoint = 'countries'
    response = get_response(endpoint)
    print(response)