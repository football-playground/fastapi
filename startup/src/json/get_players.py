from lib.api import get_response
from lib.etc import append_json
from lib.postgres import PostgresConnector
import os
from threading import Thread
from time import time, sleep
from math import ceil

def append_players():
    
    def thread_task(id_list, thread_count):
        for index in id_list:
            try:
                start_time = time()

                endpoint = 'players'
                id = index[0]
                for page in range (1, 6):
                    params = {"team": id, "season": 2023, "page":page}
                    response = get_response(endpoint, params)
                    dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/players/players_{id}_{thread_count}_{page}.json"
                    append_json(response, dir)
                
                end_time = time()
                sleep(1 - (end_time - start_time)) if end_time - start_time < 1 else True
            except Exception as E:
                raise ValueError(E)
    
    conn = PostgresConnector(database='football')
    query = "SELECT DISTINCT team_id FROM teams ORDER BY team_id ASC"
    returned = conn.fetchall(query=query)
    
    cnt = ceil(len(returned) / 14)
    thread_list = [returned[(i*cnt):(i+1)*cnt] for i in range(14)]
    
    thread_count = 1
    for thread in thread_list:
        single_thread = Thread(target=thread_task, args=(thread, thread_count))
        thread_count += 1
        single_thread.start()
        