from __future__ import annotations
import requests
import pandas as pd


def get_player_id(
    last_name : str = None,
    api_key : str = None
    ) -> pd.DataFrame:

    url = f"https://api-football-v1.p.rapidapi.com/v2/players/search/{last_name}"
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': api_key
        }
    
    player_search_rsp = requests.request("GET", url, headers = headers)
    player_search_df = pd.json_normalize(player_search_rsp.json()['api']['players'])
    return player_search_df


def player_stats(id : int, api_key : str, szn: str | None = None) -> pd.DataFrame:
    if szn is not None:
        url = f"https://api-football-v1.p.rapidapi.com/v2/players/player/{id}/{szn}"
    else:
        url = f"https://api-football-v1.p.rapidapi.com/v2/players/player/{id}"
        
    headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }

    player_stat_rsp = requests.request("GET", url, headers = headers)
    player_stat_df = pd.json_normalize(player_stat_rsp.json()['api']['players'])

    return player_stat_df


def get_last_fixtures(team_id : int, api_key : str, num_fixts : int = 5) -> pd.DataFrame:
    
    url = f"https://api-football-v1.p.rapidapi.com/v2/fixtures/team/{team_id}/last/{num_fixts}"
        
    headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }

    last_fixture_rsp = requests.request("GET", url, headers = headers)
    last_fixture_df = pd.json_normalize(last_fixture_rsp.json()['api']['fixtures'])
    return last_fixture_df

def get_next_fixtures(team_id : int, api_key : str, num_fixts : int = 5) -> pd.DataFrame:
    
    url = f"https://api-football-v1.p.rapidapi.com/v2/fixtures/team/{team_id}/next/{num_fixts}"
        
    headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }

    next_fixture_rsp = requests.request("GET", url, headers = headers)
    next_fixture_df = pd.json_normalize(next_fixture_rsp.json()['api']['fixtures'])
    return next_fixture_df


