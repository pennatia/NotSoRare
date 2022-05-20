from __future__ import annotations

import json
import pandas as pd
import requests





key = 'Your token Here'
last_name = 'tonali'

def player_search(
    last_name : str = None,
    api_key : str = None
    ):

    url = f"https://api-football-v1.p.rapidapi.com/v2/players/search/{last_name}"
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': key
        }
    
    rsp = requests.request("GET", url, headers = headers)
    return rsp.text

trial = player_search(last_name = last_name, api_key = key)

print(trial)