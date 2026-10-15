from pathlib import Path
import pytest
from tvshows.main import main


def test_main_success(tmp_path: Path, monkeypatch) -> None:
    """Test that the main function runs successfully and returns 0 when everything works as expected."""
    class FakeSource:
        def __init__(self, url, timeout):
            pass
        def fetch(self):
            # This fake fetch method returns a list of TVShow objects for testing purposes.
            from tvshows.model import TVShow
            return [TVShow(name="Test Show", language="English", genres=["Drama"], rating={"average": 8.5}, premiered="2020-01-01")]

    monkeypatch.setattr("tvshows.main.TVMazeSource", FakeSource)
    monkeypatch.setattr("tvshows.main.write_summary", lambda summary, path: None)

    # Execute the main function and check that it returns 0 (indicating success)
    exit_code = main()
    assert exit_code == 0


def test_main_failure_exits_cleanly(monkeypatch, capsys) -> None:
    """Test that the main function prints an error message and returns 1 when a failure occurs."""
    # 1. monkeypatch the TVMazeSource.fetch method to raise an exception
    def fake_fetch_error(*args, **kwargs):
        raise RuntimeError("Download failed unexpectedly")

    monkeypatch.setattr("tvshows.main.TVMazeSource.fetch", fake_fetch_error)