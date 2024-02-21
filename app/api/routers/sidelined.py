from fastapi import APIRouter
from lib.api import *

router_sidelined = APIRouter()

@router_sidelined.get("/coachsidelined")
async def get_coach_sidelined(coach_id:int, date:str):
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return coach_sidelined(coach_id, date, kafka_conf)

@router_sidelined.get("/playersidelined")
async def get_player_sidelined(player_id:int, date:str):
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return player_sidelined(player_id, date, kafka_conf)