import pytest
import requests
from tvshows.sources import TVMazeSource


def test_tvmaze_source_connection_error(monkeypatch) -> None:
    """Test that TVMazeSource handles connection errors correctly and exits with sys.exit(1)."""
    # 1. 가짜 get 함수 정의 (ConnectionError 발생)
    def fake_get(*args, **kwargs):
        raise requests.ConnectionError("No network")

    # 2. requests.get을 가짜 함수로 교체
    monkeypatch.setattr(requests, "get", fake_get)

    # 3. TVMazeSource 인스턴스 생성 및 fetch 실행 시 SystemExit(1)이 발생하는지 검증
    source = TVMazeSource(url="https://api.tvmaze.com/shows", timeout=5)
    
    with pytest.raises(SystemExit) as exc_info:
        source.fetch()

    # 종료 코드가 1인지 확인
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