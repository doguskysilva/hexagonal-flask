import hexagonal_flask.logic.league as logic_league
from hexagonal_flask.diplomat import http_client


def english_leagues():
    english_leagues = logic_league.filter_english_leagues(
        http_client.football_league("UK")
    )
    return english_leagues
