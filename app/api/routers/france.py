from fastapi import APIRouter
from lib.api import *

router_fr = APIRouter()

@router_fr.get("/france/fixtures-ids")
async def get_fixtures_ids(league:int, season:int, date:str):
    endpoint = f"fixtures?league={league}&season={season}&from={date}&to={date}"
    
    dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/france/fixtures_ids/{date}.json"
    # 또는 dir = "hdfs경로"
    
    response = get_response(endpoint)
    
    append_json(response, dir)
    
    return get_fixture_ids(response)

@router_fr.get("/france/fixtures")
async def get_fixtures(ids:str, date:str):
    league = "france"
    return fixtures(ids, league, date)

@router_fr.get("/france/injuries")
async def get_injuries(id:str, date:str):
    league = "france"
    return injuries(id, league, date)
