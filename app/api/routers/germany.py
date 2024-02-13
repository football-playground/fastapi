from fastapi import APIRouter
from lib.api import *

router_ge = APIRouter()

@router_ge.get("/germany/fixtures-ids")
async def get_fixtures_ids(date:str):
    league = "germany"
    league_id = 78
    season = 2023
    return fixtures_ids(league, league_id, season, date)

@router_ge.get("/germany/fixtures")
async def get_fixtures(ids:str, date:str):
    league = "germany"
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return fixtures(ids, league, date, kafka_conf)

@router_ge.get("/germany/injuries")
async def get_injuries(id:str, date:str):
    league = "germany"
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return injuries(id, league, date, kafka_conf)

@router_ge.get("/germany/teamstat")
async def get_team_statistics(team_id:int, date:str):
    league = "germany"
    league_id = 78
    season = 2023
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return team_statistics(league, league_id, season, team_id, date, kafka_conf)

@router_ge.get("/germany/playerstat")
async def get_player_statistics(team_id:int, date:str):
    league = "germany"
    season = 2023
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return player_statistics(league, season, team_id, date, kafka_conf)

@router_ge.get("/germany/coachsidelined")
async def get_coach_sidelined(coach_id:int, date:str):
    league = "germany"
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return coach_sidelined(league, coach_id, date, kafka_conf)

@router_ge.get("/germany/playersidelined")
async def get_player_sidelined(player_id:int, date:str):
    league = "germany"
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return player_sidelined(league, player_id, date, kafka_conf)