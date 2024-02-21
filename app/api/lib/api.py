import requests
from lib.etc import *
from lib.kafkaproducer import *

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

def fixtures_ids(league:str, league_id:int, season:int, date:str):
    try:
        endpoint = f"fixtures?league={league_id}&season={season}&from={date}&to={date}"
        dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/{league}/fixtures_ids/{date}.json"
        # 또는 dir = "hdfs경로"
        response = get_response(endpoint)
        if len(response['response']) == 0:
            return {"status": "no data"}
        else:
            append_json(response, dir)
            return get_fixture_ids(response)
    except Exception as e:
        return  {"status": "error", "message": str(e)}
    
def fixtures(fixtures_ids:str, league:str, date:str, kafka_conf:dict):
    try:
        # Airflow에서 스트링으로 변환
        #fixtures_ids_str = "-".join(map(str, fixtures_ids))
        endpoint_str = f"fixtures?ids={fixtures_ids}"
        response = get_response(endpoint_str)
        if len(response['response']) == 0:
            return {"status": "no data"}
        else:
            # 로컬 json 저장
            dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/{league}/fixtures/{date}.json"
            append_json(response, dir)
            
            # kafka publish
            topic = league
            key = 'fixtures'
            partition = 0
            publish(kafka_conf, topic, partition, key, response)
            
            return {"status": "success", "message": f"Fixtures for {date} in league {league} successfully saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def injuries(fixtures_id:str, league:str, date:str, kafka_conf:dict):
    try:
        # Airflow에서 스트링으로 변환
        #fixtures_ids_str = "-".join(map(str, fixtures_ids))
        endpoint_str = f"injuries?fixture={fixtures_id}"
        response = get_response(endpoint_str)
        if len(response['response']) == 0:
            return {"status": "no data"}
        else:
            # 로컬 json 저장
            dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/{league}/injuries/{date}.json"
            append_json(response, dir)
            
            # kafka publish
            topic = league
            key = 'injuries'
            partition = 1
            publish(kafka_conf, topic, partition, key, response)
            
            return {"status": "success", "message": f"Injuries for {date} in league {league} successfully saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def team_statistics(league:str, league_id:int, season:int, team:int, date:str, kafka_conf:dict):
    try:
        endpoint_str = f"teams/statistics?league={league_id}&season={season}&team={team}&date={date}"
        
        # 또는 dir = "hdfs경로"
        response = get_response(endpoint_str)
        if len(response['response']) == 0:
            return {"status": "no data"}
        else:
            # 로컬 json 저장
            dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/{league}/teamstat/{team}_{date}.json"
            overwrite_json(response, dir)
            
            # kafka publish
            topic = league
            key = 'teamstat'
            partition = 2
            publish(kafka_conf, topic, partition, key, response)
            
            return {"status": "success", "message": f"Team Statistics for {date} in league {league} team {team} successfully saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def player_statistics(league:str, season:int, team:int, date:str, kafka_conf:dict):
    try:
        endpoint_str = f"players?season={season}&team={team}"
        response = get_response(endpoint_str)
        if len(response['response']) == 0:
            return {"status": "no data"}
        else:
            # 로컬 json 저장
            dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/{league}/playerstat/{team}_{date}.json"
            overwrite_json(response, dir)
            
            # kafka publish
            topic = league
            key = 'playerstat'
            partition = 3
            publish(kafka_conf, topic, partition, key, response)
            
            return {"status": "success", "message": f"Player Statistics for {date} in league {league} team {team} successfully saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def coach_sidelined(coach_id:int, date:str, kafka_conf:dict):
    try:
        endpoint_str = f"sidelined?coach={coach_id}"
        response = get_response(endpoint_str)
        if len(response['response']) == 0:
            return {"status": "no data"}
        else:
            # 로컬 json 저장
            dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/coachsidelined/{coach_id}_{date}.json"
            overwrite_json(response, dir)
            
            # kafka publish
            topic = 'sidelined'
            key = 'coachsidelined'
            partition = 4
            publish(kafka_conf, topic, partition, key, response)
            
            return {"status": "success", "message": f"Coach Sidelined for {date} in coach {coach_id} successfully saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def player_sidelined(player_id:int, date:str, kafka_conf:dict):
    try:
        endpoint_str = f"sidelined?player={player_id}"
        response = get_response(endpoint_str)
        if len(response['response']) == 0:
            return {"status": "no data"}
        else:
            # 로컬 json 저장
            dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/playersidelined/{player_id}_{date}.json"
            overwrite_json(response, dir)
            
            # kafka publish
            topic = 'sidelined'
            key = 'playersidelined'
            partition = 5
            publish(kafka_conf, topic, partition, key, response)
            
            return {"status": "success", "message": f"Player Sidelined for {date} in player {player_id} successfully saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    endpoint = 'countries'
    response = get_response(endpoint)
    print(response)