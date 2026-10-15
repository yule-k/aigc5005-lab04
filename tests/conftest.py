from pathlib import Path
import json
import pytest
from tvshows.model import TVShow


@pytest.fixture
def sample_show() -> TVShow:
    """Fixture that provides a sample TVShow object for testing."""
    return TVShow(
        name="Stranger Things",
        language="English",
        genres=["Sci-Fi", "Drama"],
        rating={"average": 8.7},
        premiered="2016-07-15",
    )


@pytest.fixture
def sample_shows() -> list[TVShow]:
    """Fixture that provides a list of sample TVShow objects for testing."""
    return [
        TVShow(
            name="Show A",
            language="English",
            genres=["Drama", "Sci-Fi"],
            rating={"average": 8.0},
            premiered="2015-05-10",
        ),
        TVShow(
            name="Show B",
            language="English",
            genres=["Drama"],
            rating={"average": 9.0},
            premiered="2018-02-20",
        ),
        TVShow(
            name="Show C",
            language="Korean",
            genres=["Comedy"],
            rating={"average": 7.5},
            premiered="2021-01-15",
        ),
        TVShow(
            name="Show D",
            language="English",
            genres=None,
            rating=None,
            premiered=None,
        ),
    ]


@pytest.fixture
def sample_json_file(tmp_path: Path) -> Path:
    """Fixture that provides a temporary JSON file path and data (utilizing tmp_path)"""
    path = tmp_path / "shows.json"
    data = [
        {
            "name": "The Office",
            "language": "English",
            "genres": ["Comedy"],
            "rating": {"average": 8.9},
            "premiered": "2005-03-24",
        }
    ]
    path.write_text(json.dumps(data), encoding="utf-8")
    return path