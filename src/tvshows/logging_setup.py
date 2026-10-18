"""Logging configuration for the command line program."""

import logging


def configure_logging(level: str) -> None:
    """Send log messages to the terminal, at the given level or above."""
    numeric = getattr(logging, level.upper(), logging.INFO)
    if not isinstance(numeric, int):
        numeric = logging.INFO
    logging.basicConfig(
        level=numeric,
        format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    )
