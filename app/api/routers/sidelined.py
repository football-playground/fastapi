from fastapi import APIRouter
from lib.api import *

router_sidelined = APIRouter()

@router_sidelined.get("/coachsidelined")
async def get_coach_sidelined(date:str):
    kafka_conf = {'bootstrap.servers': 'localhost:9092'}
    return coach_sidelined(date, kafka_conf)

@router_sidelined.get("/playersidelined")
async def get_player_sidelined(date:str):
    kafka_conf = {'bootstrap.servers': 'localhost:9092', 'compression.type': 'snappy', 'message.max.bytes': 52428800}
    return player_sidelined(date, kafka_conf)