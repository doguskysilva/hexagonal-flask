from hexagonal_flask.diplomat import http_out
import hexagonal_flask.logic.league as logic_league


def english_leagues():
    english_leagues = logic_league.filter_english_leagues(
        http_out.football_league("UK")
    )
    return english_leagues
