#%%
import requests
import json
import pandas as pd

token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjZTFhM2U3MS0wOWJlLTRlZWMtYjU2MC1lZGUwOGVlNmY5ZTMiLCJzY3AiOiJ1c2VyIiwiYXVkIjoiYXBwIiwiaWF0IjoxNjUxMDc4NTU3LCJleHAiOiIxNjgyNjM1NTA5IiwianRpIjoiZjBlNWE1NWEtNjkxYi00ODQwLTgzOGUtMjAyOTQ2YWNjMDJiIn0._v_uv3MB4rxasORoJge7NJ8tlBWqXGLwuT9y-941nOg"
headers = {"content-type" : "application/json", "Authorization" : token, "JWT-AUD": 'Cost Analysis'}

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.sorare.com/graphql', json={'query': query}, headers = headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
        
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
query = """
query{
	player(slug: "fikayo-tomori"){
    slug
  	cards(rarities: limited){
      nodes{
        name
        assetId
        canBuy
        slug
        rarity
        serialNumber
        priceRange{
          min
          max
        }
        publicMinPrice
        privateMinPrice
        
      }
      }
  }}
"""

result = run_query(query) # Execute the query
#%%
df = pd.json_normalize(result['data']['player']['cards']['nodes'])

# %%
