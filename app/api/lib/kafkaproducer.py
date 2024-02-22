from confluent_kafka import Producer
from fastapi import FastAPI, HTTPException
import json

def publish(kafka_conf:dict, topic:str, partition, key:str, data):
    try:
        producer = Producer(**kafka_conf)
        if partition == None:
            producer.produce(topic, key=key, value=json.dumps(data))
            producer.flush()
        else:
            producer.produce(topic, key=key, partition=partition, value=json.dumps(data))
            producer.flush()
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

