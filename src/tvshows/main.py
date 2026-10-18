# thin entry point; error message
import logging
import sys

from tvshows.aggregations import (
    AverageRatingByLanguage,
    GenreCount,
    ShowsPerDecade,
)
from tvshows.config import load_settings
from tvshows.logging_setup import configure_logging
from tvshows.report import (
    build_run_info,
    build_summary,
    write_summary,
)
from tvshows.sources import TVMazeSource

logger = logging.getLogger(__name__)


def main(argv: list[str] | None = None) -> int:
    """Main function to records, compute, and write a summary."""
    configure_logging("INFO")
    try:
        settings = load_settings()
        logging.getLogger().setLevel(settings.log_level)
        source = TVMazeSource(settings.url, settings.timeout)
        shows = source.fetch()

        aggregations = [
            GenreCount(),
            AverageRatingByLanguage(),
            ShowsPerDecade(),
        ]
        summary = build_summary(
            shows, settings.url, aggregations, settings.seed, settings.sample_size
        )
        output_path = settings.output_dir / "summary.json"
        settings.output_dir.mkdir(parents=True, exist_ok=True)
        write_summary(summary, output_path)
        write_summary(build_run_info(settings), settings.output_dir / "run_info.json")

        logger.info("Read %d records.", len(shows))
        logger.info("Summary written to %s", settings.output_dir)

        return 0

    except Exception as e:
        logger.error("An error occurred during execution: %s", e)
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
