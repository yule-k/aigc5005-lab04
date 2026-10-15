#thin entry point; error message

from tvshows.config import URL, TIMEOUT, OUTPUT
from tvshows.sources import TVMazeSource
from tvshows.aggregations import (
    GenreCount,
    AverageRatingByLanguage,
    ShowsPerDecade,
)
from tvshows.report import build_summary, write_summary


def main():
    """Main function to fetch TV show records, compute aggregations, and write a summary."""
    source = TVMazeSource(URL, TIMEOUT)
    shows = source.fetch()

    aggregations = [
        GenreCount(),
        AverageRatingByLanguage(),
        ShowsPerDecade(),
    ]

    summary = build_summary(shows, URL, aggregations)
    write_summary(summary, OUTPUT)

    print(f"Read {len(shows)} records.")
    print(f"Summary written to {OUTPUT}")


if __name__ == "__main__":
    #Run the main function if this script is executed directly.
    main()