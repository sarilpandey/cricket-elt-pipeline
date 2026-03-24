import requests

API_URL = "https://api.cricapi.com/v1/currentMatches"
API_KEY = "YOUR_API_KEY"

def fetch_cricket_data():
    response = requests.get(API_URL, params={"apikey": API_KEY})
    data = response.json()

    matches = []

    for match in data.get("data", []):
        matches.append({
            "date": match.get("date"),
            "team1": match.get("teams", [None, None])[0],
            "team2": match.get("teams", [None, None])[1],
            "venue": match.get("venue")
        })

    return matches
