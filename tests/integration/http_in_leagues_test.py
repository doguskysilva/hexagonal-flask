import json

from tests.integration.helpers import response_json

def test_get_empty_leagues(client, requests_mock):
    requests_mock.get('https://api-football-v1.p.rapidapi.com/v3/leagues', json=[])

    response = client.get('/')
    data = response_json(response)
    
    assert response.status_code == 200
    assert data == []

def test_get_english_leagues(client, requests_mock):
    requests_mock.get('https://api-football-v1.p.rapidapi.com/v3/leagues', json=[
        {"country": "UK", "name": "English League"},
        {"country": "BR", "name": "Campeonato Brasileiro"},
        {"country": "FR", "name": "League 1"}
    ])

    response = client.get('/')
    data = response_json(response)
    
    assert response.status_code == 200
    assert data == [
        {"country": "UK", "name": "English League"}
    ]