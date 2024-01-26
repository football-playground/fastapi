from lib.api import get_response
from lib.etc import append_json
from lib.postgres import PostgresConnector
import os
from threading import Thread
from time import time, sleep
from math import ceil

def append_transfers():
    
    def thread_task(id_list, thread_count):
        for index in id_list:
            start_time = time()
            
            endpoint = 'transfers'
            id = index[0]
            params = {"player": id}
            response = get_response(endpoint, params)
            dir = f"{os.path.dirname(os.path.abspath(__file__))}/../../datas/transfers/transfers_{id}_{thread_count}.json"
            append_json(response, dir)
            
            end_time = time()
            sleep(1 - (end_time - start_time)) if end_time - start_time < 1 else True
    
    conn = PostgresConnector(database='football')
    query = "SELECT DISTINCT player_id FROM players ORDER BY player_id ASC"
    returned = conn.fetchall(query=query)
    
    cnt = ceil(len(returned) / 14)
    thread_list = [returned[(i*cnt):(i+1)*cnt] for i in range(14)]
    
    # for thread in thread_list:
    #     print(str(thread[0][0]) + " " + str(thread[-1][0]))
    
    thread_count = 1
    for thread in thread_list:
        single_thread = Thread(target=thread_task, args=(thread, thread_count))
        thread_count += 1
        single_thread.start()
