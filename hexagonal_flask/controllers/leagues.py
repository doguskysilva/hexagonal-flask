from hexagonal_flask.diplomat import http_out 

def english_leagues():
    english_leagues = http_out.football_league("uk")
    return english_leagues