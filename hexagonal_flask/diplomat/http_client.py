import requests


def football_league(country: str):
    url = "https://api-football-v1.p.rapidapi.com/v3/leagues"
    headers = {
        "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
        "x-rapidapi-key": "SIGN-UP-FOR-KEY",
    }

    response = requests.request("GET", url, headers=headers)

    return response.json() if response.status_code == 200 else []
