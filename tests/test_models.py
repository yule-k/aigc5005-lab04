import json
from pathlib import Path

import pytest

from tvshows.errors import DataError
from tvshows.model import TVShow, tvshow_from_dict


def test_tvshow_creation_with_defaults():
    """Test that a TVShow object is created correctly."""
    show = TVShow(name="Breaking Bad")
    assert show.name == "Breaking Bad"
    assert show.genres == []  # Missing genres should default to an empty list
    assert show.rating is None  # Missing rating should default to None
    assert show.year is None
    assert show.decade is None


def test_tvshow_with_full_data(sample_show: TVShow):
    """Test that a TVShow object is created correctly with full data."""
    assert sample_show.name == "Stranger Things"
    assert sample_show.language == "English"
    assert sample_show.genres == ["Sci-Fi", "Drama"]
    assert sample_show.rating == 8.7
    assert sample_show.year == 2016
    assert sample_show.decade == 2010


def test_tvshow_from_dict(sample_json_file: Path):
    """Test that a TVShow object is created correctly from a dictionary."""
    raw_data = json.loads(sample_json_file.read_text(encoding="utf-8"))
    show = tvshow_from_dict(raw_data[0])

    assert show.name == "The Office"
    assert show.genres == ["Comedy"]
    assert show.rating == 8.9
    assert show.year == 2005
    assert show.decade == 2000


def test_tvshow_from_dict_without_name():
    """Test that a record without a name raises DataError."""
    with pytest.raises(DataError, match="missing data"):
        tvshow_from_dict({"genres": ["Drama"]})
