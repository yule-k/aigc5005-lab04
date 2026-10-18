import pytest
import requests

from tvshows.sources import TVMazeSource
from tvshows.errors import DataError, SourceError


def test_tvmaze_source_connection_error(monkeypatch) -> None:
    """Test that TVMazeSource handles connection errors correctly."""

    # 1. Define a dummy get function (raises ConnectionError)
    def fake_get(*args, **kwargs):
        raise requests.ConnectionError("No network")

    # 2. Replace requests.get with a mock function.
    monkeypatch.setattr(requests, "get", fake_get)

    # 3. Verify whether SystemExit(1) occurs.
    source = TVMazeSource(url="https://api.tvmaze.com/shows", timeout=5)

    with pytest.raises(SourceError, match="Unable to reach"):
        source.fetch()


def test_tvmaze_source_http_error(monkeypatch) -> None:
    """Test that TVMazeSource handles HTTP errors correctly."""

    class FakeResponse:
        def raise_for_status(self):
            raise requests.HTTPError("404 Not Found")

    def fake_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)

    source = TVMazeSource(url="https://api.tvmaze.com/shows", timeout=5)

    with pytest.raises(SourceError, match="HTTP error"):
        source.fetch()

def test_tvmaze_source_bad_data(monkeypatch) -> None:
    """Test that a response that is not a list raises DataError."""

    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"not": "a list"}

    def fake_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)

    source = TVMazeSource(url="https://api.tvmaze.com/shows", timeout=5)

    with pytest.raises(DataError, match="Expected a list"):
        source.fetch()