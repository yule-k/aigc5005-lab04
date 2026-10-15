# build and write the summary

import json


def build_summary(shows, source_url, aggregations):
    """Build a summary dictionary from TV show records."""

    summary = {"source_URL": source_url, "records_processed": len(shows)}

    for aggregation in aggregations:
        result = aggregation.compute(shows)
        summary[aggregation.name] = result

    return summary


def write_summary(summary, output_path):
    """Write the summary to a JSON file."""

    output_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
