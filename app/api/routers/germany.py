from fastapi import APIRouter
from lib.api import *

router_ge = APIRouter()

@router_ge.get("/germany/fixtures-ids")
async def get_fixtures_ids(league:int, season:int, date:str):
    endpoint = f"fixtures?league={league}&season={season}&from={date}&to={date}"
    
    dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/germany/fixtures_ids/{date}.json"
    # 또는 dir = "hdfs경로"
    
    response = get_response(endpoint)
    
    append_json(response, dir)
    
    return get_fixture_ids(response)

@router_ge.get("/germany/fixtures")
async def get_fixtures(ids:str, date:str):
    league = "germany"
    return fixtures(ids, league, date)

@router_ge.get("/germany/injuries")
async def get_injuries(id:str, date:str):
    league = "germany"
    return injuries(id, league, date)
