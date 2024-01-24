import requests
from lib.etc import get_config_values

def get_response(endpoint:str, params:dict = None):
    # set url
    url = f'https://v3.football.api-sports.io/{endpoint}?'
    if params != None:
        for key, value in params.items():
            url += f"{key}={value}&"

    # set headers
    [api_key] = get_config_values([('api', 'key')])
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }

    # get response
    response = requests.get(url, headers=headers).json()
    
    return response

if __name__ == "__main__":
    endpoint = 'countries'
    response = get_response(endpoint)
    print(response)