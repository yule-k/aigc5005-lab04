from tvshows.model import TVShow, tvshow_from_dict


def test_tvshow_creation_with_defaults():
    """Test that a TVShow object is created correctly with default values when optional fields are missing."""
    show = TVShow(name="Breaking Bad")
    assert show.name == "Breaking Bad"
    assert show.genres == []  # Missing genres should default to an empty list
    assert show.rating is None  # Missing rating should default to None
    assert show.year is None
    assert show.decade is None


def test_tvshow_with_full_data():
    """Test that a TVShow object is created correctly with full data."""
    show = TVShow(
        name="Stranger Things",
        language="English",
        genres=["Sci-Fi", "Drama"],
        rating={"average": 8.7},
        premiered="2016-07-15",
    )
    assert show.name == "Stranger Things"
    assert show.language == "English"
    assert show.genres == ["Sci-Fi", "Drama"]
    assert show.rating == 8.7
    assert show.year == 2016
    assert show.decade == 2010


def test_tvshow_from_dict():
    """Test that a TVShow object is created correctly from a dictionary."""
    data = {
        "name": "The Office",
        "language": "English",
        "genres": ["Comedy"],
        "rating": {"average": 8.9},
        "premiered": "2005-03-24",
    }
    show = tvshow_from_dict(data)
    assert show.name == "The Office"
    assert show.genres == ["Comedy"]
    assert show.rating == 8.9
    assert show.year == 2005
    assert show.decade == 2000