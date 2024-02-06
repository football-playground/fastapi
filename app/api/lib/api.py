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
    
def fixtures(fixtures_ids:str, league:str, date:str):
    try:
        # Airflow에서 스트링으로 변환
        #fixtures_ids_str = "-".join(map(str, fixtures_ids))
        endpoint_str = f"fixtures?ids={fixtures_ids}"
        dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/{league}/fixtures/{date}.json"
        # 또는 dir = "hdfs경로"
        response = get_response(endpoint_str)
        if len(response['response']) == 0:
            return {"status": "no data"}
        else:
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
        if len(response['response']) == 0:
            return {"status": "no data"}
        else:
            append_json(response, dir)
            return {"status": "success", "message": f"Injuries for {date} in league {league} successfully saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def team_statistics(league:str, league_id:int, season:int, team:int, date:str):
    try:
        endpoint_str = f"teams/statistics?league={league_id}&season={season}&team={team}&date={date}"
        dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/{league}/teamstat/{team}_{date}.json"
        # 또는 dir = "hdfs경로"
        response = get_response(endpoint_str)
        if len(response['response']) == 0:
            return {"status": "no data"}
        else:
            append_json(response, dir)
            return {"status": "success", "message": f"Team Statistics for {date} in league {league} team {team} successfully saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def player_statistics(league:str, season:int, team:int, date:str):
    try:
        endpoint_str = f"players?season={season}&team={team}"
        dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/{league}/playerstat/{team}_{date}.json"
        # 또는 dir = "hdfs경로"
        response = get_response(endpoint_str)
        if len(response['response']) == 0:
            return {"status": "no data"}
        else:
            append_json(response, dir)
            return {"status": "success", "message": f"Player Statistics for {date} in league {league} team {team} successfully saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def coach_sidelined(league:str, coach_id:int, date:str):
    try:
        endpoint_str = f"sidelined?coach={coach_id}"
        dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/{league}/coachsidelined/{coach_id}_{date}.json"
        # 또는 dir = "hdfs경로"
        response = get_response(endpoint_str)
        if len(response['response']) == 0:
            return {"status": "no data"}
        else:
            overwrite_json(response, dir)
            return {"status": "success", "message": f"Coach Sidelined for {date} in league {league} coach {coach_id} successfully saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def player_sidelined(league:str, player_id:int, date:str):
    try:
        endpoint_str = f"sidelined?player={player_id}"
        dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/{league}/playersidelined/{player_id}_{date}.json"
        # 또는 dir = "hdfs경로"
        response = get_response(endpoint_str)
        if len(response['response']) == 0:
            return {"status": "no data"}
        else:
            overwrite_json(response, dir)
            return {"status": "success", "message": f"Player Sidelined for {date} in league {league} player {player_id} successfully saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    endpoint = 'countries'
    response = get_response(endpoint)
    print(response)