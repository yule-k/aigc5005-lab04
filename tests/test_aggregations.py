import pytest

from tvshows.aggregations import (
    AverageRatingByLanguage,
    GenreCount,
    ShowsPerDecade,
)
from tvshows.model import TVShow


def test_genre_count(sample_shows: list[TVShow]) -> None:
    """Make sure the GenreCount aggregation correctly counts the number of shows in each genre."""
    agg = GenreCount()
    result = agg.compute(sample_shows)
    assert result == {"Drama": 2, "Sci-Fi": 1, "Comedy": 1}


def test_average_rating_by_language(sample_shows: list[TVShow]) -> None:
    """Make sure the AverageRatingByLanguage aggregation correctly calculates the average rating for each language."""
    agg = AverageRatingByLanguage()
    result = agg.compute(sample_shows)
    # English: (8.0 + 9.0) / 2 = 8.5
    # Korean: 7.5 / 1 = 7.5
    assert result == {"English": 8.5, "Korean": 7.5}


def test_shows_per_decade(sample_shows: list[TVShow]) -> None:
    """Make sure the ShowsPerDecade aggregation correctly counts the number of shows premiered in each decade."""
    agg = ShowsPerDecade()
    result = agg.compute(sample_shows)
    assert result == {2010: 2, 2020: 1}


@pytest.mark.parametrize(
    "aggregation_instance, expected_name",
    [
        (GenreCount(), "count by genres"),
        (AverageRatingByLanguage(), "average ratings by language"),
        (ShowsPerDecade(), "shows premiered per decade"),
    ],
)
def test_aggregation_names(aggregation_instance, expected_name: str) -> None:
    """Make sure that the name attribute of each aggregation class is set correctly."""
    assert aggregation_instance.name == expected_name
