def filter_english_leagues(leagues: list):
    return list(
        filter(lambda league: league["country"].upper() == "UK", leagues)
    )
