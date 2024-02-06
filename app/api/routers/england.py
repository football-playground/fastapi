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
    return fixtures(ids, league, date)

@router_en.get("/england/injuries")
async def get_injuries(id:str, date:str):
    league = "england"
    return injuries(id, league, date)

@router_en.get("/england/teamstat")
async def get_team_statistics(team_id:int, date:str):
    league = "england"
    league_id = 39
    season = 2023
    return team_statistics(league, league_id, season, team_id, date)

@router_en.get("/england/playerstat")
async def get_player_statistics(team_id:int, date:str):
    league = "england"
    season = 2023
    return player_statistics(league, season, team_id, date)

@router_en.get("/england/coachsidelined")
async def get_coach_sidelined(coach_id:int, date:str):
    league = "england"
    return coach_sidelined(league, coach_id, date)

@router_en.get("/england/playersidelined")
async def get_player_sidelined(player_id:int, date:str):
    league = "england"
    return player_sidelined(league, player_id, date)