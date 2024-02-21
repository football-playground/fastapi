from fastapi import APIRouter
from lib.api import *

router_en = APIRouter()

@router_en.get("/england/fixtures-ids")
async def get_fixtures_ids(date:str):
    league = "england"
    league_id = 39
    season = 2023
    return fixtures_ids(league, league_id, season, date)
    
@router_en.get("/england/fixtures")
async def get_fixtures(ids:str, date:str):
    league = "england"
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return fixtures(ids, league, date, kafka_conf)

@router_en.get("/england/injuries")
async def get_injuries(id:str, date:str):
    league = "england"
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return injuries(id, league, date, kafka_conf)

@router_en.get("/england/teamstat")
async def get_team_statistics(team_id:int, date:str):
    league = "england"
    league_id = 39
    season = 2023
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return team_statistics(league, league_id, season, team_id, date, kafka_conf)

@router_en.get("/england/playerstat")
async def get_player_statistics(team_id:int, date:str):
    league = "england"
    season = 2023
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return player_statistics(league, season, team_id, date, kafka_conf)

