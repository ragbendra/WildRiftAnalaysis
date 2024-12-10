import requests

API_KEY = "RGAPI-3c4044a1-b00b-4b44-a11f-b303b87dce59"
BASE_URL = "https://api.riotgames.com"

def get_match_data(match_id):
    response = requests.get(f"{BASE_URL}/wildrift/matches/{match_id}", headers={"X-Riot-Token": API_KEY})
    return response.json()
