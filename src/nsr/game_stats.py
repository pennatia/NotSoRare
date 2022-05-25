from __future__ import annotations
import requests
import pandas as pd
from nsr.player_info import get_last_fixtures


def get_fixture_stats(fixture_id: int, player_id : int, api_key : str):
    url = f"https://api-football-v1.p.rapidapi.com/v2/players/fixture/{fixture_id}"

    headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }

    fixture_stats = requests.request("GET", url, headers = headers)
    fixture_stats_df = pd.json_normalize(fixture_stats.json()['api']['players'])
    player_fixture_stats = fixture_stats_df[fixture_stats_df['player_id'] == player_id]
    return player_fixture_stats

def get_last_x_stats(team_id : int, player_id : int, api_key : str, num_fixts: int = 5):
    last_fixtures = get_last_fixtures(team_id, api_key, num_fixts)

    f_stats = pd.DataFrame()
    
    for i in range(num_fixts):
        f_id = last_fixtures.iloc[i]['fixture_id']
        temp_df = get_fixture_stats(f_id,player_id,api_key)
        temp_df['team_1'] = last_fixtures.iloc[i]['homeTeam.team_name']
        temp_df['team_2'] = last_fixtures.iloc[i]['awayTeam.team_name']
        f_stats = pd.concat([f_stats, temp_df]).reset_index(drop=True)
    
    return f_stats
