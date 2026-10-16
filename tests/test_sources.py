import pytest
import requests

from tvshows.sources import TVMazeSource


def test_tvmaze_source_connection_error(monkeypatch) -> None:
    """Test that TVMazeSource handles connection errors correctly and exits with sys.exit(1)."""

    # 1. Define a dummy get function (raises ConnectionError)
    def fake_get(*args, **kwargs):
        raise requests.ConnectionError("No network")

    # 2. Replace requests.get with a mock function.
    monkeypatch.setattr(requests, "get", fake_get)

    # 3. Verify whether SystemExit(1) occurs when creating a TVMazeSource instance and executing fetch.
    source = TVMazeSource(url="https://api.tvmaze.com/shows", timeout=5)

    with pytest.raises(SystemExit) as exc_info:
        source.fetch()

    # Check if the exit code is 1.
    assert exc_info.value.code == 1


def test_tvmaze_source_http_error(monkeypatch) -> None:
    """Test that TVMazeSource handles HTTP errors correctly and exits with sys.exit(1)."""

    class FakeResponse:
        def raise_for_status(self):
            raise requests.HTTPError("404 Not Found")

    def fake_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)

    source = TVMazeSource(url="https://api.tvmaze.com/shows", timeout=5)

    with pytest.raises(SystemExit) as exc_info:
        source.fetch()

    assert exc_info.value.code == 1
