import json

from tests.integration.helpers import response_json

def test_get_empty_leagues(client):
    response = client.get('/')
    data = response_json(response)
    
    assert response.status_code == 200
    assert data == []