# build and write the summary

import json
from pathlib import Path

from tvshows.aggregations import Aggregation
from tvshows.model import TVShow


def build_summary(
    shows: list[TVShow], source_url: str, aggregations: list[Aggregation]
) -> dict:
    """Build a summary dictionary from TV show records."""

    summary = {"source_URL": source_url, "records_processed": len(shows)}

    for aggregation in aggregations:
        result = aggregation.compute(shows)
        summary[aggregation.name] = result

    return summary


def write_summary(summary: dict, output_path: Path) -> None:
    """Write the summary to a JSON file."""

    output_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
