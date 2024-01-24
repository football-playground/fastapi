import psycopg2
from lib.etc import get_config_values

class PostgresConnector:
    def __init__(self, database:str):
        [host, port, user, password] = get_config_values([("postgres", "host"), 
                                                          ("postgres", "port"), 
                                                          ("postgres", "user"), 
                                                          ("postgres", "password")])
        self.conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
    
    def commit(self, query:str, values:tuple=None):
        cursor = self.conn.cursor()

        # execute
        if values == None:
            cursor.execute(query)
        else:
            cursor.execute(query, values)
        
        # commit
        self.conn.commit()
        cursor.close()

    def fetchall(self, query:str, values:tuple=None):
        cursor = self.conn.cursor()
        
        # execute
        if values == None:
            cursor.execute(query)
        else:
            cursor.execute(query, values)
        
        # fetchall
        rows = cursor.fetchall()
        cursor.close()
        
        return rows
    
    def fetchone(self, query:str, values:tuple=None):
        cursor = self.conn.cursor()
        
        # execute
        if values == None:
            cursor.execute(query)
        else:
            cursor.execute(query, values)
        
        # fetchone
        rows = cursor.fetchone()
        cursor.close()
        
        return rows
    
    def close(self):
        self.conn.close()
    