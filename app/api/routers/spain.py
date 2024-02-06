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
    return fixtures(ids, league, date)

@router_sp.get("/spain/injuries")
async def get_injuries(id:str, date:str):
    league = "spain"
    return injuries(id, league, date)

@router_sp.get("/spain/teamstat")
async def get_team_statistics(team_id:int, date:str):
    league = "spain"
    league_id = 140
    season = 2023
    return team_statistics(league, league_id, season, team_id, date)

@router_sp.get("/spain/playerstat")
async def get_player_statistics(team_id:int, date:str):
    league = "spain"
    season = 2023
    return player_statistics(league, season, team_id, date)

@router_sp.get("/spain/coachsidelined")
async def get_coach_sidelined(coach_id:int, date:str):
    league = "spain"
    return coach_sidelined(league, coach_id, date)

@router_sp.get("/spain/playersidelined")
async def get_player_sidelined(player_id:int, date:str):
    league = "spain"
    return player_sidelined(league, player_id, date)