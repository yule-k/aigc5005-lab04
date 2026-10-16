# fetching; only module using requests
import logging
import sys

import requests

from tvshows.model import tvshow_from_dict

logger = logging.getLogger(__name__)

class TVMazeSource:
    """Download TV show records from the TVMaze API and return a list of TVShow instances."""

    def __init__(self, url, timeout=10):
        """Initialize the TVMazeSource with a URL and timeout."""
        self.url = url
        self.timeout = timeout

    def fetch(self) -> list[dict]:
        """Fetch TV show records from the API and return a list of TVShow instances."""
        try:
            response = requests.get(self.url, self.timeout)
            response.raise_for_status()
        except (requests.ConnectionError, requests.Timeout):
            logger.error("Unable to reach %s", self.url)
            sys.exit(1)
        except requests.HTTPError:
            logger.error("Error: HTTP error occurred while fetching data from %s", self.url)
            sys.exit(1)

        raw_data = response.json()
        shows = []
        for show_data in raw_data:
            show = tvshow_from_dict(show_data)
            shows.append(show)
        return shows
