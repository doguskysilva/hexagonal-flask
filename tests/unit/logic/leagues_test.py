import pytest

from hexagonal_flask.logic.league import filter_english_leagues


@pytest.mark.parametrize(
    "all_leagues,expected",
    [
        ([], []),
        ([{"country": "br"}, {"country": "mx"}], []),
        ([{"country": "br"}, {"country": "uk"}], [{"country": "uk"}]),
    ],
)
def test_filter_english_leagues(all_leagues, expected):
    assert filter_english_leagues(all_leagues) == expected
