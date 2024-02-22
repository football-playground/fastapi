from fastapi import APIRouter
from lib.api import *

router_sp = APIRouter()

@router_sp.get("/spain/fixtures-ids")
async def get_fixtures_ids(date:str):
    league = "spain"
    league_id = 140
    season = 2023
    return fixtures_ids(league, league_id, season, date)

@router_sp.get("/spain/fixtures")
async def get_fixtures(ids:str, date:str):
    league = "spain"
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return fixtures(ids, league, date, kafka_conf)

@router_sp.get("/spain/injuries")
async def get_injuries(id:str, date:str):
    league = "spain"
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return injuries(id, league, date, kafka_conf)

@router_sp.get("/spain/teamstat")
async def get_team_statistics(date:str):
    league = "spain"
    league_id = 140
    season = 2023
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return team_statistics(league, league_id, season, date, kafka_conf)

@router_sp.get("/spain/playerstat")
async def get_player_statistics(date:str):
    league = "spain"
    league_id = 140
    season = 2023
    kafka_conf = {'bootstrap.servers': 'localhost:9092', 'compression.type': 'snappy', 'message.max.bytes': 52428800}
    return player_statistics(league, league_id, season, date, kafka_conf)
