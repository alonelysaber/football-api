import requests
import pandas as pd
from dotenv import load_dotenv
import os
import json
 
load_dotenv()
 
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
 
league_id = 140 # La Liga 2025
team_id = 541 # real madrid
 
endpoint_url = "https://v3.football.api-sports.io/fixtures"

params={
    "league" : league_id,
    "team" : team_id,
    "status" : "FT",
    "season" : "2023"
}

headers = {
  'x-rapidapi-key': API_KEY,
  'x-rapidapi-host': API_URL
}
 
response = requests.request("GET", endpoint_url, headers=headers, params=params)
 
data = response.json()
data = data["response"][0]

print(json.dumps(data, indent=2))