# build and write the summary

import json
import platform
import random
from importlib import metadata
from pathlib import Path

from tvshows.aggregations import Aggregation
from tvshows.config import Settings
from tvshows.model import TVShow


def build_summary(
    shows: list[TVShow],
    source_url: str,
    aggregations: list[Aggregation],
    seed: int,
    sample_size: int,
) -> dict:
    """Build a summary dictionary from TV show records."""

    summary = {
        "source_URL": source_url,
        "records_processed": len(shows),
        "featured_shows": get_featured_shows(shows, seed, sample_size),
    }

    for aggregation in aggregations:
        result = aggregation.compute(shows)
        summary[aggregation.name] = result

    return summary


def write_summary(summary: dict, output_path: Path) -> None:
    """Write the summary to a JSON file."""

    output_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")


def build_run_info(settings: Settings) -> dict:
    """Record the settings and tool versions used for this run."""
    return {
        "settings": {
            "url": settings.url,
            "timeout": settings.timeout,
            "output_dir": str(settings.output_dir),
            "seed": settings.seed,
            "sample_size": settings.sample_size,
            "log_level": settings.log_level,
        },
        "python": platform.python_version(),
        "pytest": metadata.version("pytest"),
        "mypy": metadata.version("mypy"),
        "ruff": metadata.version("ruff"),
    }


def get_featured_shows(shows: list[TVShow], seed: int, sample_size: int) -> list[dict]:
    """Select a deterministic random sample of shows using the given seed."""
    rng = random.Random(seed)
    k = min(len(shows), sample_size)
    sampled = rng.sample(shows, k)
    return [
        show.to_dict() if hasattr(show, "to_dict") else vars(show) for show in sampled
    ]


def write_run_info(run_info: dict, output_dir: Path) -> None:
    """Write the run metadata to run_info.json."""
    output_dir.mkdir(parents=True, exist_ok=True)
    info_path = output_dir / "run_info.json"
    info_path.write_text(json.dumps(run_info, indent=2), encoding="utf-8")
