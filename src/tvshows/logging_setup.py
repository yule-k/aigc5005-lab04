"""Logging configuration for the command line program."""

import logging

from tvshows.main import main  # 또는 로그를 찍는 함수나 main 함수


def configure_logging(level: str) -> None:
    """Send log messages to the terminal, at the given level or above."""
    numeric = getattr(logging, level.upper(), logging.INFO)
    if not isinstance(numeric, int):
        numeric = logging.INFO
    logging.basicConfig(
        level=numeric,
        format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
        force=True,
    )


def test_logged_message(caplog):
    """Test whether messages are correctly logged at the specified log level."""

    with caplog.at_level(logging.INFO):
        try:
            main(["--config", "config/tvshows.toml"])
        except SystemExit:
            pass

    assert any("Read" in record.message for record in caplog.records)
