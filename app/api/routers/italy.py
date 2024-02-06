from fastapi import APIRouter
from lib.api import *

router_it = APIRouter()

@router_it.get("/italy/fixtures-ids")
async def get_fixtures_ids(date:str):
    league = "italy"
    league_id = 135
    season = 2023
    return fixtures_ids(league, league_id, season, date)

@router_it.get("/italy/fixtures")
async def get_fixtures(ids:str, date:str):
    league = "italy"
    return fixtures(ids, league, date)

@router_it.get("/italy/injuries")
async def get_injuries(id:str, date:str):
    league = "italy"
    return injuries(id, league, date)

@router_it.get("/italy/teamstat")
async def get_team_statistics(team_id:int, date:str):
    league = "italy"
    league_id = 135
    season = 2023
    return team_statistics(league, league_id, season, team_id, date)

@router_it.get("/italy/playerstat")
async def get_player_statistics(team_id:int, date:str):
    league = "italy"
    season = 2023
    return player_statistics(league, season, team_id, date)

@router_it.get("/italy/coachsidelined")
async def get_coach_sidelined(coach_id:int, date:str):
    league = "italy"
    return coach_sidelined(league, coach_id, date)

@router_it.get("/italy/playersidelined")
async def get_player_sidelined(player_id:int, date:str):
    league = "italy"
    return player_sidelined(league, player_id, date)