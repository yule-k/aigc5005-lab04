# thin entry point; error message

from tvshows.aggregations import (
    AverageRatingByLanguage,
    GenreCount,
    ShowsPerDecade,
)
from tvshows.config import OUTPUT, TIMEOUT, URL
from tvshows.report import build_summary, write_summary
from tvshows.sources import TVMazeSource


def main() -> int:
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

    return 0


if __name__ == "__main__":
    # Run the main function if this script is executed directly.
    main()
