# fetching; only module using requests
import logging

import requests

from tvshows.errors import DataError, SourceError
from tvshows.model import TVShow, tvshow_from_dict

logger = logging.getLogger(__name__)


class TVMazeSource:
    """Download TV show records and return"""

    def __init__(self, url: str, timeout: float = 10) -> None:
        """Initialize the TVMazeSource with a URL and timeout."""
        self.url = url
        self.timeout = timeout

    def fetch(self) -> list[TVShow]:
        """Fetch TV show records from the API and return."""
        try:
            response = requests.get(self.url, timeout=self.timeout)
            response.raise_for_status()
        except (requests.ConnectionError, requests.Timeout) as error:
            raise SourceError(f"Unable to reach {self.url}") from error
        except requests.HTTPError as error:
            raise SourceError(
                f"HTTP error while fetching data from {self.url}"
            ) from error

        try:
            raw_data = response.json()
        except ValueError as error:
            raise DataError(f"{self.url} did not return valid JSON.") from error
        if not isinstance(raw_data, list):
            raise DataError(f"Expected a list of shows from {self.url}.")
        logger.debug("Received %d records from %s", len(raw_data), self.url)

        shows: list[TVShow] = []
        for show_data in raw_data:
            show = tvshow_from_dict(show_data)
            shows.append(show)
        return shows
